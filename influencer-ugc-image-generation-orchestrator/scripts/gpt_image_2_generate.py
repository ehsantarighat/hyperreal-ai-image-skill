#!/usr/bin/env python3
import argparse
import base64
import json
import os
import sys
from datetime import datetime
from pathlib import Path

try:
    from openai import OpenAI
except ImportError:
    print("Missing dependency: openai. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

SIZE_MAP = {
    "1:1": "1024x1024",
    "4:5": "1024x1280",
    "9:16": "1024x1792",
    "16:9": "1536x864",
}

UGC_HINTS = {
    "raw": "The image should feel like raw, authentic smartphone-native UGC with believable imperfection.",
    "polished": "The image should feel like polished influencer-style UGC: natural, social-native, realistic, but not a glossy studio ad.",
    "premium": "The image should feel like premium UGC: elevated lifestyle quality while still believable and creator-native, not a synthetic campaign render.",
}

def read_prompt(args):
    if args.prompt:
        return args.prompt.strip()
    if args.prompt_file:
        return Path(args.prompt_file).read_text(encoding="utf-8").strip()
    if not args.scene:
        raise ValueError("Either --prompt, --prompt-file, or --scene is required.")
    return compose_prompt_from_scene(args)

def compose_prompt_from_scene(args):
    aspect = args.aspect or "4:5"
    lens = args.lens or "35mm"
    camera_angle = args.camera_angle or "eye-level"
    ugc_tier = (args.ugc_tier or "polished").lower()
    usage = args.usage or "Instagram post"

    parts = [
        "Create a hyperrealistic influencer-style UGC product photo.",
        "Use the exact same person from the provided model reference image. Preserve facial identity, face shape, hair appearance, skin tone, and age impression. Do not beautify, stylize, or replace the person with a generic model.",
        "Use the exact same product from the provided product reference image. Preserve packaging structure, geometry, material, dominant colors, closure design, and visible branding layout. Do not redesign, distort, or invent branding elements.",
        f"Intended use: {usage}.",
        f"Scene: {args.scene.strip()}",
        f"Composition: Create a believable lifestyle composition in {aspect} format with the product clearly visible while still feeling natural and creator-led.",
        f"Camera: {camera_angle} camera angle, {lens} lens, realistic perspective, natural depth of field.",
        "Lighting: natural, physically plausible lighting with coherent shadows and realistic highlights.",
        "Realism: natural skin texture, visible pores, realistic hair strands, believable hand anatomy, convincing grip around the product, realistic scale, and accurate contact shadows.",
        UGC_HINTS.get(ugc_tier, UGC_HINTS["polished"]),
        "Avoid: plastic skin, over-retouched face, CGI look, generic AI influencer aesthetics, distorted fingers, floating product, altered branding, fake label text, surreal lighting, over-produced ad polish.",
    ]
    if args.extra_direction:
        parts.append(f"Additional direction: {args.extra_direction.strip()}")
    return "\n\n".join(parts)

def ensure_api_key():
    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set.", file=sys.stderr)
        sys.exit(2)

def build_client():
    return OpenAI()

def save_outputs(result, outdir: Path, prompt_text: str, metadata: dict, output_format: str):
    outdir.mkdir(parents=True, exist_ok=True)
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")

    prompt_path = outdir / f"prompt_{ts}.txt"
    prompt_path.write_text(prompt_text, encoding="utf-8")

    saved_images = []
    data_items = getattr(result, "data", None) or []
    suffix = "png" if output_format == "png" else ("jpg" if output_format == "jpeg" else "webp")

    for i, item in enumerate(data_items, start=1):
        b64 = getattr(item, "b64_json", None)
        if not b64 and isinstance(item, dict):
            b64 = item.get("b64_json")
        if not b64:
            continue
        image_bytes = base64.b64decode(b64)
        img_path = outdir / f"generated_{ts}_{i}.{suffix}"
        with open(img_path, "wb") as f:
            f.write(image_bytes)
        saved_images.append(str(img_path))

    meta = {
        "timestamp_utc": ts,
        "model": metadata["model"],
        "mode": metadata["mode"],
        "prompt_file": str(prompt_path),
        "prompt": prompt_text,
        "settings": metadata["settings"],
        "saved_images": saved_images,
    }
    meta_path = outdir / f"metadata_{ts}.json"
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"prompt_file": str(prompt_path), "metadata_file": str(meta_path), "saved_images": saved_images}

def main():
    parser = argparse.ArgumentParser(description="Generate influencer-style UGC images via GPT Image 2.")
    parser.add_argument("--model-image", required=False, help="Path to the model reference image.")
    parser.add_argument("--product-image", required=False, help="Path to the product reference image.")
    parser.add_argument("--reference-image", action="append", default=[], help="Additional reference image path(s).")
    parser.add_argument("--scene", help="Scene description.")
    parser.add_argument("--prompt", help="Fully custom prompt text.")
    parser.add_argument("--prompt-file", help="Path to a file containing the final prompt.")
    parser.add_argument("--usage", help="Target use such as Instagram post, story, ad, etc.")
    parser.add_argument("--aspect", default="4:5", choices=["1:1", "4:5", "9:16", "16:9"], help="Target aspect ratio.")
    parser.add_argument("--size", help="Explicit size override, e.g. 1024x1280.")
    parser.add_argument("--quality", default="high", choices=["low", "medium", "high"], help="Generation quality.")
    parser.add_argument("--output-format", default="png", choices=["png", "jpeg", "webp"], help="Image format.")
    parser.add_argument("--background", default="auto", help="Optional background mode if supported by the model.")
    parser.add_argument("--n", type=int, default=1, help="Number of images to generate.")
    parser.add_argument("--ugc-tier", default="polished", choices=["raw", "polished", "premium"], help="UGC style tier.")
    parser.add_argument("--lens", help="Lens suggestion, e.g. 35mm.")
    parser.add_argument("--camera-angle", help="Camera angle, e.g. eye-level or slight three-quarter.")
    parser.add_argument("--extra-direction", help="Additional generation direction.")
    parser.add_argument("--outdir", required=True, help="Directory to save outputs.")
    parser.add_argument("--model", default="gpt-image-2", help="Image model. Default: gpt-image-2.")
    args = parser.parse_args()

    ensure_api_key()
    prompt_text = read_prompt(args)
    client = build_client()
    outdir = Path(args.outdir)
    size = args.size or SIZE_MAP.get(args.aspect, "1024x1280")

    image_paths = []
    if args.model_image:
        image_paths.append(args.model_image)
    if args.product_image:
        image_paths.append(args.product_image)
    image_paths.extend(args.reference_image)

    if image_paths:
        image_files = []
        try:
            for p in image_paths:
                image_files.append(open(p, "rb"))
            result = client.images.edit(
                model=args.model,
                image=image_files,
                prompt=prompt_text,
                size=size,
                quality=args.quality,
                output_format=args.output_format,
                n=args.n,
            )
            mode = "reference-image-generation"
        finally:
            for f in image_files:
                try:
                    f.close()
                except Exception:
                    pass
    else:
        result = client.images.generate(
            model=args.model,
            prompt=prompt_text,
            size=size,
            quality=args.quality,
            output_format=args.output_format,
            n=args.n,
        )
        mode = "prompt-only-generation"

    metadata = {
        "model": args.model,
        "mode": mode,
        "settings": {
            "aspect": args.aspect,
            "size": size,
            "quality": args.quality,
            "output_format": args.output_format,
            "n": args.n,
            "ugc_tier": args.ugc_tier,
            "usage": args.usage,
            "lens": args.lens,
            "camera_angle": args.camera_angle,
        },
    }

    saved = save_outputs(result, outdir, prompt_text, metadata, args.output_format)
    print(json.dumps(saved, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
