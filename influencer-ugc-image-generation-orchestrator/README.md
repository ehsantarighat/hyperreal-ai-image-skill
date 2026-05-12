# Influencer UGC Image Generation Orchestrator

This Claude Skill produces **hyperrealistic influencer-style UGC product images** from:
- a model reference image
- a product reference image
- a scene description

Unlike a prompt-only skill, this package includes a direct execution helper for **GPT Image 2**.

## What it does

- Preserves model identity across generations
- Preserves product structure, packaging, and visual fidelity
- Converts a scene brief into a production-ready image prompt
- Uses GPT Image 2 for actual image generation
- Supports reference-image workflows with both model and product images
- Saves generated images, prompts, and metadata

## Folder layout

```text
influencer-ugc-image-generation-orchestrator/
├── SKILL.md
├── README.md
├── requirements.txt
├── generator_profiles/
│   └── gpt-image-2.yaml
├── scripts/
│   └── gpt_image_2_generate.py
├── references/
│   ├── camera-lens-guide.md
│   ├── failure-diagnosis.md
│   ├── model-consistency.md
│   ├── product-preservation.md
│   ├── realism-control.md
│   └── ugc-style-guide.md
├── templates/
│   ├── campaign-consistency-template.md
│   ├── guided-generate-template.md
│   └── quick-generate-template.md
└── examples/
    ├── beverage-product-example.md
    └── skincare-product-example.md
```

## Install in Claude Code

Copy this folder into:

```text
~/.claude/skills/influencer-ugc-image-generation-orchestrator
```

Or use the repository-level installer script:

```bash
curl -fsSL https://raw.githubusercontent.com/ehsantarighat/hyperreal-ai-image-skill/main/install-ugc-orchestrator.sh | bash
```

## Dependency

```bash
pip install -r ~/.claude/skills/influencer-ugc-image-generation-orchestrator/requirements.txt
```

## Environment variable

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

## Example command

```bash
python ~/.claude/skills/influencer-ugc-image-generation-orchestrator/scripts/gpt_image_2_generate.py \
  --model-image /absolute/path/to/model.jpg \
  --product-image /absolute/path/to/product.png \
  --scene "A bright home bathroom in the morning. The model holds the product near her face for a polished influencer-style Instagram post." \
  --aspect 4:5 \
  --ugc-tier polished \
  --quality high \
  --n 1 \
  --outdir /absolute/path/to/output_run
```

## Output files

The script saves:
- generated image files
- the exact prompt used
- metadata JSON with settings and output paths

## Notes

- Use only reference images you have the right to use.
- This skill is designed for consent-based model references and commercial/product visuals.
- Exact tiny typography on product labels may still require final post-production correction when brand-critical.
