---
name: pptx-icons-images-compression
description: >-
  Insert scalable icons (SVG), source/crop/mask images cleanly, and compress media so the .pptx isn't 80MB — picture format, crop-to-shape, set transparency
---

# pptx-icons-images-compression

Insert > Icons gives line/SVG icons that scale without pixelation and recolor via Graphics Format > Graphics Fill (use theme colors). Convert an SVG icon to a Shape (Graphics Format > Convert to Shape) to recolor individual paths. For photos: Picture Format > Crop to fill a placeholder, or Crop > Crop to Shape for masks; Picture Format > Transparency or Set Transparent Color for knockouts; Remove Background for cutouts. The big win is size: Picture Format > Compress Pictures > uncheck 'Apply only to this picture', set 150 ppi (on-screen) or 220 ppi (print), and check 'Delete cropped areas of pictures' — cropping only hides pixels until you do this. A deck with full-res phone photos easily hits 50-100MB; compression drops it 5-10x. In python-pptx: `slide.shapes.add_picture(path, x, y, width=...)` (omit height to keep aspect). Pitfall: stretching a small raster looks blurry on a 4K projector — use SVG/icons for anything that scales, raster only for photographs. Save a copy before compressing if print fidelity matters.

**Tools:** Insert > Icons (SVG); Picture Format > Crop/Compress Pictures; Graphics Format > Convert to Shape; python-pptx add_picture
