# Hyperreal AI Image Skill

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

After this repository is published on GitHub, install globally with:

```bash
curl -fsSL https://raw.githubusercontent.com/ehsantarighat/hyperreal-ai-image-skill/main/install.sh | bash
```

This installs the skill into:

```text
~/.claude/skills/hyperreal-ai-image-skill
```

## Install from another owner or branch

```bash
REPO=your-username/hyperreal-ai-image-skill BRANCH=main bash -c "$(curl -fsSL https://raw.githubusercontent.com/your-username/hyperreal-ai-image-skill/main/install.sh)"
```

## Manual install

```bash
git clone https://github.com/ehsantarighat/hyperreal-ai-image-skill.git
mkdir -p ~/.claude/skills
cp -R hyperreal-ai-image-skill/hyperreal-ai-image-skill ~/.claude/skills/
```

Then restart Claude Code.

## Claude.ai web upload

For Claude.ai web, zip the `hyperreal-ai-image-skill/` folder and upload it from **Customize > Skills**.

Correct ZIP structure:

```text
hyperreal-ai-image-skill.zip
└── hyperreal-ai-image-skill/
    ├── SKILL.md
    ├── resources/
    ├── templates/
    └── examples/
```

## Example usage

Ask Claude:

```text
Create a hyperrealistic UGC prompt for a consistent AI model promoting a skincare serum in a bathroom mirror selfie. Make it natural, believable, and not over-polished.
```

Or:

```text
Build a Character Bible and 10 image prompts for a realistic AI lifestyle model with a premium but candid Instagram aesthetic.
```

## Notes

- The skill is designed for fictional AI models or images where you have consent and rights to use references.
- Avoid impersonating real people or public figures.
- Disclose AI-generated personas where appropriate for commercial or public-facing use.
