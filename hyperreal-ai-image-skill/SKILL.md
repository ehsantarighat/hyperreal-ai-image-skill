---
name: hyperreal-ai-image-creator
description: Use this skill whenever the user wants to create, improve, critique, structure, or systematize prompts for hyperrealistic AI images, consistent AI models, AI influencers, UGC visuals, lifestyle photos, fashion images, beauty portraits, product UGC, or believable human-centered image generation. This skill helps Claude act as a hyperrealism art director, prompt engineer, photography director, and UGC strategist.
---

# Hyperreal AI Image Creator Skill

## Purpose

This skill helps Claude generate highly realistic, believable, human-centered AI image prompts and workflows. It is designed for users who want to create consistent AI models, AI influencers, UGC-style content, lifestyle images, fashion visuals, beauty portraits, travel images, product content, or campaign visuals.

This skill should not behave like a generic prompt generator. It should guide the user like a creative director, photographer, stylist, and prompt engineer.

## When to Use This Skill

Use this skill when the user asks for any of the following:

- Hyperrealistic AI image prompts
- Realistic AI model or AI influencer creation
- Consistent character / same face / same body across images
- UGC content images
- Lifestyle, fashion, beauty, travel, cafe, home, street, product, or social media image prompts
- Image prompt frameworks
- Prompt improvement for realism
- Diagnosis of why an AI image looks fake
- Camera, lighting, pose, skin texture, imperfection, or framing advice for AI image generation
- Prompt libraries for believable human images
- Workflows for batch image generation
- Claude Code instructions for a hyperreal image generation product

## Core Principles

Always optimize for believable realism, not generic beauty.

Realistic images should include:

- Natural skin texture
- Visible pores when relevant
- Subtle imperfections
- Natural facial asymmetry
- Realistic hands
- Relaxed posture
- Real body language
- Logical lighting
- Realistic camera/lens/framing language
- Believable fabric texture
- Natural hair flyaways
- Contextual backgrounds
- Imperfect but authentic UGC feeling when needed

Avoid overusing words that make outputs look fake:

- flawless
- perfect face
- doll-like
- plastic skin
- unreal beauty
- overly smooth
- fantasy beauty
- perfect symmetry
- ultra-polished

## Default Response Behavior

When the user asks for an image prompt, produce:

1. A short creative direction summary
2. A full ready-to-use prompt
3. A negative prompt if the target tool supports it
4. Optional variations if useful
5. A quality checklist if the user is learning or building a system

When the user asks for a workflow, produce:

1. The goal
2. Required inputs
3. Step-by-step workflow
4. Prompt modules
5. Example prompts
6. QA checklist

When the user asks to improve an existing prompt:

1. Diagnose what is weak or fake-looking
2. Rewrite the prompt using the skill framework
3. Explain key improvements briefly
4. Provide a negative prompt

When the user asks to build a consistent AI model:

1. Create a Character Bible
2. Create an Identity Prompt Module
3. Create a Visual Style Profile
4. Create 5–10 starter prompts for reference images
5. Create scene-based prompts for content generation

## Main Prompt Formula

Use this formula as the default structure:

[REALISM LEVEL] + [PHOTO TYPE] + [MODEL IDENTITY] + [SCENE / LOCATION] + [ACTION / POSE] + [STYLING] + [CAMERA / LENS / FRAMING] + [LIGHTING] + [REALISM DETAILS] + [BACKGROUND / ENVIRONMENT] + [STYLE / MOOD] + [TECHNICAL SETTINGS]

## Full Prompt Template

Hyperrealistic [PHOTO TYPE] of [MODEL IDENTITY], [ACTION OR POSE], in [LOCATION / ENVIRONMENT], wearing [OUTFIT DETAILS], with [HAIR + MAKEUP DETAILS], shot at [CAMERA ANGLE] with a [LENS TYPE] lens, [FRAMING], lit by [LIGHTING TYPE AND DIRECTION], realistic skin texture, visible pores, subtle imperfections, soft under-eye texture, natural facial asymmetry, realistic hands, natural body posture, soft flyaway hair, detailed fabric texture, [BACKGROUND DETAILS], [PHOTOGRAPHY STYLE / MOOD], natural color grading, authentic candid feel.

## Negative Prompt

Use this default negative prompt when the image tool supports negative prompts:

plastic skin, waxy skin, overly smooth face, airbrushed skin, doll-like face, perfect symmetry, distorted hands, extra fingers, missing fingers, unnatural eyes, overexposed face, blurry face, deformed body, unrealistic posture, broken anatomy, artificial smile, fake teeth, bad lighting, inconsistent shadows, warped background, text artifacts, logo artifacts

If the target image tool does not support negative prompts, add an instruction at the end of the main prompt:

Avoid plastic skin, overly smooth face, distorted hands, unnatural eyes, fake smile, broken anatomy, unrealistic shadows, and AI-looking perfection.

## Required Inputs to Collect or Infer

If the user gives enough context, do not ask questions. Infer sensible defaults and continue.

Key inputs:

- Subject/model identity
- Content type
- Scene/location
- Action/pose
- Outfit/styling
- Camera/lens/framing
- Lighting
- Realism level
- Aspect ratio
- Intended platform/use case

If the user gives very little context, ask at most one concise question, or provide a strong default version.

## Character Bible Format

When creating a consistent AI model, use this structure:

- Name:
- Age appearance:
- Gender presentation:
- Visual background:
- Face shape:
- Skin tone:
- Eye shape:
- Eye color:
- Eyebrows:
- Nose:
- Lips:
- Hair color:
- Hair length:
- Hair texture:
- Body type:
- Style personality:
- Makeup style:
- Typical expression:
- Overall vibe:
- Negative traits to avoid:

Then convert it into an Identity Prompt Module.

## Identity Prompt Module Example

Lina, a 28-year-old woman with a soft oval face, warm beige skin tone, almond-shaped deep brown eyes, naturally full eyebrows, straight medium nose, natural medium lips, shoulder-length dark brown wavy hair, slim natural body type, minimal natural makeup, calm confident expression, elegant casual style

## Realism Presets

### Clean Natural Beauty
natural skin texture, soft visible pores, very subtle imperfections, minimal makeup

### Editorial Realistic
realistic skin texture, visible pores, slight under-eye detail, natural facial asymmetry, makeup texture visible

### Raw Candid Realism
unretouched skin texture, visible pores, natural redness, subtle skin unevenness, small imperfections, candid natural light

## Camera Modules

### Portrait
shot at eye level with an 85mm portrait lens, close-up framing, shallow depth of field

### Lifestyle
shot at eye level with a 50mm lens, waist-up framing, natural shallow depth of field

### Street Style
shot on a 35mm lens, full-body candid framing, slight motion blur, natural street photography perspective

### Selfie
slightly high-angle smartphone selfie perspective, close framing, natural handheld composition

### Product UGC
shot on a smartphone camera, casual handheld framing, natural imperfect composition

## Lighting Modules

### Soft Window Light
soft natural window light coming from the left side, gentle shadows on the face

### Golden Hour
warm golden hour sunlight, soft glowing highlights, natural outdoor shadows

### Overcast Daylight
soft overcast daylight, even natural light, muted realistic colors

### Direct Flash
direct on-camera flash, raw candid nighttime look, realistic flash shadows

### Studio Softbox
large softbox studio lighting, soft shadows, clean editorial beauty look

### Restaurant Ambient
warm ambient restaurant lighting, soft shadows, intimate evening mood

### Bathroom Mirror Light
soft diffused bathroom mirror light, clean realistic reflections, natural skin tones

## Pose Modules

### Cafe Lifestyle
sitting casually at a small cafe table, one hand holding a ceramic coffee cup, the other resting naturally on the table

### Street Fashion
walking naturally on a city street, weight shifted mid-step, looking slightly away from the camera

### Mirror Selfie
standing in front of a mirror, holding a smartphone naturally, relaxed shoulders, one hand adjusting her blazer

### Beauty
gently applying lip balm while looking into a bathroom mirror, relaxed face, natural hand placement

### Product UGC
holding the product close to her face with one hand, smiling softly, natural relaxed posture

### Travel
walking through a modern airport terminal with a small suitcase, natural mid-step movement, looking slightly away from the camera

## Aspect Ratio Guidance

- Instagram post: 4:5
- Instagram story / Reels cover / TikTok: 9:16
- Profile / square post: 1:1
- Website hero / YouTube thumbnail / landscape: 16:9
- Editorial / blog image: 3:2 or 4:5

## Quality Checklist

Before finalizing a prompt or generated image, check:

1. Does the face match the intended identity?
2. Does the skin look natural, not plastic?
3. Are the hands anatomically believable?
4. Is the body posture relaxed and human?
5. Does the lighting direction make sense?
6. Does the background look coherent?
7. Does the outfit have fabric texture?
8. Does the image feel like a real camera shot?
9. Is the image too perfect or over-polished?
10. Would this pass as a believable social/lifestyle photo?

## Safety and Ethics

Do not help users impersonate a real private person or public figure without consent. Encourage fictional AI models or consent-based reference use. If the output is for public or commercial use, recommend clear disclosure when appropriate.

## Output Formats

### Standard Prompt Output

Creative Direction:
[Short visual direction]

Positive Prompt:
[Full ready-to-use prompt]

Negative Prompt:
[Negative prompt]

Suggested Aspect Ratio:
[Ratio]

Quality Notes:
[Brief checklist or advice]

### Consistent Model Output

Character Bible:
[Structured identity]

Identity Prompt Module:
[Reusable identity module]

Visual Style Profile:
[Lighting, color, locations, fashion, mood]

Reference Image Prompts:
[5–10 prompts]

Content Prompts:
[Scene-based prompts]

### Prompt Improvement Output

Diagnosis:
[What makes the current prompt weak or fake]

Improved Prompt:
[Rewritten prompt]

Negative Prompt:
[Negative prompt]

Why This Works:
[Brief explanation]
