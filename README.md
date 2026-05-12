# Hyperreal AI Image Skills

This repository now contains **two Claude Skills** for realistic AI image workflows:

1. **`hyperreal-ai-image-skill`** — a prompt/directing skill for hyperrealistic AI models, AI influencers, and UGC-style image prompting.
2. **`influencer-ugc-image-generation-orchestrator`** — a generation-oriented skill that uses **GPT Image 2** to produce actual influencer-style UGC product images from a model reference image, a product reference image, and a scene description.

---

# 1) Hyperreal AI Image Skill

A Claude Skill for generating hyperrealistic, believable AI model and UGC image prompts.

This skill helps Claude act as a **hyperrealism art director, prompt engineer, photographer, stylist, and UGC strategist**. It guides Claude to create structured prompts for realistic AI models with consistent identity, natural skin texture, believable lighting, camera/lens control, natural posing, and commercial UGC workflows.

## What it does

- Builds consistent AI model identities
- Generates hyperrealistic prompt structures
- Adds realism controls for skin, texture, imperfections, lighting, framing, and body language
- Produces UGC-style prompts for social, beauty, fashion, lifestyle, and product content
- Includes reusable prompt modules and templates
- Includes a quality checklist for evaluating AI-generated images

## Folder structure

```text
hyperreal-ai-image-skill/
  SKILL.md
  resources/
    prompt-modules.md
  templates/
    prompt-templates.md
  examples/
    example-request-response.md
install.sh
README.md
```

## One-line install for Claude Code

```bash
curl -fsSL https://raw.githubusercontent.com/ehsantarighat/hyperreal-ai-image-skill/main/install.sh | bash
```

This installs the prompt-focused skill into:

```text
~/.claude/skills/hyperreal-ai-image-skill
```

---

# 2) Influencer UGC Image Generation Orchestrator

A Claude Skill for producing **actual hyperrealistic influencer-style UGC product images** using **GPT Image 2**.

It is designed for use cases where the user provides:

- a **model reference image**
- a **product reference image**
- a **scene description**

and expects a **generated visual output**, not just a prompt.

## What it does

- Preserves model identity across image generations
- Preserves product structure, packaging, and visual fidelity
- Converts scene descriptions into production-ready prompts
- Uses GPT Image 2 through a helper script for actual image generation
- Supports reference-image workflows with both model and product images
- Saves generated images, prompt files, and metadata JSON

## Folder structure

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

## One-line install for Claude Code

```bash
curl -fsSL https://raw.githubusercontent.com/ehsantarighat/hyperreal-ai-image-skill/main/install-ugc-orchestrator.sh | bash
```

This installs the GPT Image 2 generation skill into:

```text
~/.claude/skills/influencer-ugc-image-generation-orchestrator
```

## Install dependency

```bash
pip install -r ~/.claude/skills/influencer-ugc-image-generation-orchestrator/requirements.txt
```

## Set OpenAI API key

```bash
export OPENAI_API_KEY="your_openai_api_key_here"
```

## Example direct execution

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

---

## Claude.ai web upload

For Claude.ai web, zip the desired skill folder and upload it from **Customize > Skills**.

Prompt-focused skill:

```text
hyperreal-ai-image-skill.zip
└── hyperreal-ai-image-skill/
    ├── SKILL.md
    ├── resources/
    ├── templates/
    └── examples/
```

Generation-oriented skill:

```text
influencer-ugc-image-generation-orchestrator.zip
└── influencer-ugc-image-generation-orchestrator/
    ├── SKILL.md
    ├── README.md
    ├── requirements.txt
    ├── scripts/
    ├── references/
    ├── templates/
    ├── examples/
    └── generator_profiles/
```

---

## Notes

- Use only images you have the right to use.
- These skills are designed for fictional AI models or consent-based references.
- Avoid impersonating real private people or public figures without permission.
- Exact tiny typography on product packaging may still require final post-production correction when brand-critical.
