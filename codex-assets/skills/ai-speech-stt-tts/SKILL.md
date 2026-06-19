---
name: ai-speech-stt-tts
description: >-
  Add speech to LLM apps — transcription (Whisper/STT), text-to-speech, streaming, diarization, and latency budgeting for voice agents — use to build voice interfaces or process audio.
---

# ai-speech-stt-tts

Two pipelines. BATCH (transcribe a file): Whisper or a hosted STT returns text; request word-level timestamps for subtitles/search and segment timestamps for chaptering; supply a domain prompt/vocabulary hint to bias jargon and names. For multi-speaker audio, add diarization (who-spoke-when). VOICE AGENT (realtime): either chain STT→LLM→TTS or use a speech-to-speech/Realtime API that skips text round-trips for lower latency. Latency is the product: budget sub-~800ms perceived response — use Voice Activity Detection for endpointing (detect when the user stopped), STREAM the STT partials, STREAM LLM tokens, and STREAM TTS so audio starts before generation finishes; let user speech barge-in/interrupt playback. Pick TTS by naturalness vs latency vs voice-cloning needs. Pitfalls: hallucinated transcription on silence/noise (filter with VAD/confidence), wrong-language autodetect (pin the language), and cutting off the user by endpointing too aggressively. Common mistake: a non-streaming chain that feels laggy — stream every stage and overlap them. Always show a live transcript for trust and correction.

**Tools:** Whisper / streaming STT, realtime/speech-to-speech APIs, TTS, VAD, diarization, word timestamps
