---
name: pptx-speaker-notes-presenter
description: >-
  Write effective speaker notes, set up Presenter View (next-slide, timer, notes), rehearse timings, and export notes pages — without notes ever showing on screen
---

# pptx-speaker-notes-presenter

Notes live per-slide (View > Notes pane or Notes Page view for full-page layout). Write talking-point cues, not your bullets verbatim — the audience reads slides, you read the room. Presenter View (Slide Show > Use Presenter View, or it auto-engages with a second display) shows current slide, next slide preview, notes, elapsed timer, and pen/laser/zoom tools — the audience sees only the slideshow. If it's on the wrong monitor, use 'Display Settings > Swap'. Rehearse Timings records how long you spend per slide so you can pace; Slide Show > Record narrates + timestamps for self-running kiosks. Export: File > Export > Create Handouts, or Print > Notes Pages to give a slide+notes PDF. In python-pptx: `slide.notes_slide.notes_text_frame.text = '...'` to inject notes programmatically (great for auto-generated decks with a script). Pitfall: people paste their entire script into notes and read it — defeats the point and the timer shows you're overrunning. Test Presenter View on the actual rig before the talk; HDMI display ordering surprises live.

**Tools:** View > Notes; Notes Page view; Slide Show > Presenter View / Rehearse Timings; python-pptx notes_slide.notes_text_frame
