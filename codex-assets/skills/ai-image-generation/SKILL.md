---
name: ai-image-generation
description: >-
  Generate and edit images with diffusion/text-to-image models: prompt structure, negative prompts, img2img/inpainting, control (ControlNet/reference), and seeds — use to create or modify visuals programmatically.
---

# ai-image-generation

Structure image prompts as subject + descriptors + style + composition + lighting (concrete nouns and art-style references beat vague adjectives). Negative prompts exclude artifacts ('blurry, extra fingers, text') on models that support them. Modes: text-to-image (from scratch); img2img (transform an input — denoising 'strength' controls how far from the source, low=subtle edit, high=reimagine); inpainting (mask a region and regenerate only it — for object removal/replacement); outpainting (extend canvas). For precise control use ControlNet/structure conditioning (pose, depth, edges, scribble) or reference/identity conditioning to keep a subject consistent across images. Fix the seed for reproducibility and to iterate one variable at a time; CFG/guidance scale trades prompt-adherence vs creativity/realism (too high = oversaturated/fried). Generate batches and select. Pitfalls: text-in-image and precise counts are weak on many models (use a model with strong typography for logos/UI), and fine details degrade at low step counts. Watch licensing/usage rights and add provenance metadata (C2PA) for shipped assets. Common mistake: cranking guidance to force adherence and getting artifacts — lower it and improve the prompt instead.

**Tools:** text-to-image APIs, SDXL/FLUX, negative prompts, img2img strength, inpainting/outpainting, ControlNet, seed/CFG
