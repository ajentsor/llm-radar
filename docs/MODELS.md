# AI Models Reference

**Last Updated:** 2026-01-07T08:30:16+00:00

**Summary:** 84 OpenAI models including GPT-5.2, GPT-5.1, O-series reasoning models, and GPT-4o variants; 8 Anthropic Claude models up to version 4.5; 32 Google Gemini models including 3.0 preview and 2.5 series are accessible via API.

## OpenAI

**Website:** https://openai.com  
**API Documentation:** https://platform.openai.com/docs

| Model ID | Type | Status | Input Modalities |
|----------|------|--------|------------------|
| `chatgpt-image-latest` | image | active | text, image |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio |
| `gpt-5.2-chat-latest` | chat | active | text |
| `gpt-5.2-pro` | chat | active | text |
| `gpt-5.2` | chat | active | text |
| `gpt-5.1-codex-max` | chat | active | text |
| `gpt-5.1-codex` | chat | active | text |
| `gpt-5.1` | chat | active | text |
| `gpt-5.1-chat-latest` | chat | active | text |
| `gpt-5-search-api` | chat | active | text |
| `gpt-5-pro` | chat | active | text |
| `gpt-5-codex` | chat | active | text |
| `gpt-5` | chat | active | text |
| `gpt-5-chat-latest` | chat | active | text |
| `o4-mini-deep-research` | reasoning | active | text |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio |
| `gpt-4.1` | chat | active | text |
| `o4-mini` | reasoning | active | text |
| `o3` | reasoning | active | text |
| `o1-pro` | reasoning | active | text |
| `gpt-4o-mini-search-preview` | chat | preview | text, image |
| `gpt-4o-search-preview` | chat | preview | text, image |
| `o3-mini` | reasoning | active | text |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio |
| `o1` | reasoning | active | text |
| `gpt-4o-audio-preview` | audio | preview | text, audio |
| `gpt-4o-realtime-preview` | audio | preview | text, audio |
| `chatgpt-4o-latest` | chat | active | text, image |
| `gpt-4o-mini` | chat | active | text, image |
| `gpt-4o` | chat | active | text, image |
| `gpt-4-turbo` | chat | active | text |
| `gpt-4` | chat | active | text |
| `gpt-3.5-turbo` | chat | active | text |

## Anthropic

**Website:** https://anthropic.com  
**API Documentation:** https://docs.anthropic.com

| Model ID | Type | Status | Input Modalities |
|----------|------|--------|------------------|
| `claude-opus-4-5-20251101` | chat | active | text |
| `claude-haiku-4-5-20251001` | chat | active | text |
| `claude-sonnet-4-5-20250929` | chat | active | text |
| `claude-opus-4-1-20250805` | chat | active | text |
| `claude-opus-4-20250514` | chat | active | text |
| `claude-sonnet-4-20250514` | chat | active | text |
| `claude-3-5-haiku-20241022` | chat | active | text |
| `claude-3-haiku-20240307` | chat | active | text |

## Google

**Website:** https://ai.google.dev  
**API Documentation:** https://ai.google.dev/docs

| Model ID | Type | Status | Input Modalities | Context Window |
|----------|------|--------|------------------|----------------|
| `gemini-3-pro-preview` | chat | preview | text | 1,048,576 |
| `gemini-3-flash-preview` | chat | preview | text | 1,048,576 |
| `gemini-2.5-flash` | chat | active | text | 1,048,576 |
| `gemini-2.5-pro` | chat | active | text | 1,048,576 |
| `gemini-2.5-flash-preview-tts` | audio | preview | text | 8,192 |
| `gemini-2.0-flash` | chat | active | text | 1,048,576 |

## Notes

- **Multimodal Support:** Models with image/audio input are marked in the Input Modalities column
- **Preview Models:** May have limited availability or experimental features
- **Reasoning Models:** O-series models are specialized for complex reasoning tasks
- **Audio Models:** Support text-to-speech (TTS), speech-to-text (transcription), or real-time audio interaction
- **Context Windows:** Shown for Google models where specified; null values indicate unspecified limits