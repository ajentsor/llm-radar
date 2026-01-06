# AI Models API Reference

**Last Updated:** January 6, 2026 at 08:30 UTC

**Summary:** 124 AI models available via API from OpenAI (84 models), Anthropic (8 models), and Google (32 models), including GPT-5 series, Claude 4.5, and Gemini 3.0.

## OpenAI Models

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
| `gpt-4o-mini-audio-preview` | audio | preview | text, image, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, image, audio |
| `o1` | reasoning | active | text |
| `gpt-4o-audio-preview` | audio | preview | text, image, audio |
| `gpt-4o-realtime-preview` | audio | preview | text, image, audio |
| `chatgpt-4o-latest` | chat | active | text, image |
| `gpt-4o-mini` | chat | active | text, image |
| `gpt-4o` | chat | active | text, image |
| `gpt-4-turbo` | chat | active | text |
| `gpt-4` | chat | active | text |
| `gpt-3.5-turbo` | chat | active | text |

## Anthropic Models

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

## Google Models

**API Documentation:** https://ai.google.dev/docs

| Model ID | Type | Status | Input Modalities | Context Window |
|----------|------|--------|------------------|----------------|
| `gemini-3-pro-preview` | chat | preview | text | 1M tokens |
| `gemini-3-flash-preview` | chat | preview | text | 1M tokens |
| `gemini-2.5-flash` | chat | active | text | 1M tokens |
| `gemini-2.5-pro` | chat | active | text | 1M tokens |
| `gemini-2.5-flash-preview-tts` | audio | preview | text | 8K tokens |
| `gemini-2.0-flash` | chat | active | text | 1M tokens |

---

**Note:** Models marked as `preview` may have limited availability or experimental features. Context windows shown where available (1M = 1,048,576 tokens).