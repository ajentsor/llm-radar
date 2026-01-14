# AI Models Reference

**Last Updated:** January 14, 2026 at 08:30 UTC

**Summary:** 84 OpenAI models, 8 Anthropic models, and 32 Google Gemini models are available via API, including latest GPT-5.2, Claude Opus 4.5, and Gemini 3 Pro series.

## OpenAI

[Website](https://openai.com) | [API Documentation](https://platform.openai.com/docs)

| Model ID | Type | Status | Multimodal |
|----------|------|--------|------------|
| `chatgpt-image-latest` | image | active | text → image |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text → audio |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio → text |
| `gpt-5.2-chat-latest` | chat | active | |
| `gpt-5.2-pro` | chat | active | |
| `gpt-5.2` | chat | active | |
| `gpt-5.1-codex-max` | chat | active | |
| `gpt-5.1-codex` | chat | active | |
| `gpt-5.1` | chat | active | |
| `gpt-5.1-chat-latest` | chat | active | |
| `gpt-5-search-api` | chat | active | |
| `gpt-5-pro` | chat | active | |
| `gpt-5-codex` | chat | active | |
| `gpt-5` | chat | active | |
| `gpt-5-chat-latest` | chat | active | |
| `o4-mini-deep-research` | reasoning | active | |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio → text, audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio → text, audio |
| `gpt-4.1` | chat | active | |
| `o4-mini` | reasoning | active | |
| `o3` | reasoning | active | |
| `o1-pro` | reasoning | active | |
| `gpt-4o-mini-search-preview` | chat | preview | text, image → text |
| `gpt-4o-search-preview` | chat | preview | text, image → text |
| `o3-mini` | reasoning | active | |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio → text, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio → text, audio |
| `o1` | reasoning | active | |
| `gpt-4o-realtime-preview` | audio | preview | text, audio → text, audio |
| `gpt-4o-audio-preview` | audio | preview | text, audio → text, audio |
| `chatgpt-4o-latest` | chat | active | text, image → text |
| `gpt-4o-mini` | chat | active | text, image → text |
| `gpt-4o` | chat | active | text, image → text |
| `gpt-4-turbo` | chat | active | |
| `gpt-4` | chat | active | |
| `gpt-3.5-turbo` | chat | active | |

## Anthropic

[Website](https://anthropic.com) | [API Documentation](https://docs.anthropic.com)

| Model ID | Type | Status | Multimodal |
|----------|------|--------|------------|
| `claude-opus-4-5-20251101` | chat | active | |
| `claude-haiku-4-5-20251001` | chat | active | |
| `claude-sonnet-4-5-20250929` | chat | active | |
| `claude-opus-4-1-20250805` | chat | active | |
| `claude-opus-4-20250514` | chat | active | |
| `claude-sonnet-4-20250514` | chat | active | |
| `claude-3-5-haiku-20241022` | chat | active | |
| `claude-3-haiku-20240307` | chat | active | |

## Google

[Website](https://ai.google.dev) | [API Documentation](https://ai.google.dev/docs)

| Model ID | Type | Status | Context Window | Multimodal |
|----------|------|--------|----------------|------------|
| `models/gemini-3-pro-preview` | chat | preview | 1M | |
| `models/gemini-3-flash-preview` | chat | preview | 1M | |
| `models/gemini-2.5-flash` | chat | active | 1M | |
| `models/gemini-2.5-pro` | chat | active | 1M | |
| `models/gemini-2.5-flash-preview-tts` | audio | preview | 8K | text → audio |
| `models/gemini-2.5-pro-preview-tts` | audio | preview | 8K | text → audio |
| `models/gemini-2.5-flash-lite` | chat | active | 1M | |
| `models/gemini-2.0-flash` | chat | active | 1M | |
| `models/gemini-2.0-flash-lite` | chat | active | 1M | |

## Model Types

- **chat**: Text conversation models
- **reasoning**: Advanced reasoning and problem-solving models
- **audio**: Audio processing (TTS, transcription, realtime)
- **image**: Image generation models

## Status

- **active**: Production-ready
- **preview**: Early access, may change