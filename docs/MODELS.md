# AI Models API Reference

**Last updated:** January 24, 2026  
**Summary:** 85 OpenAI models, 8 Anthropic models, and 31 Google Gemini models are accessible via API, including newest GPT-5.2, Claude 4.5, and Gemini 3 series.

## OpenAI

**Provider:** OpenAI | [Website](https://openai.com) | [API Docs](https://platform.openai.com/docs)

| Model ID | Name | Type | Status | Input Modalities |
|----------|------|------|--------|------------------|
| `gpt-5.2-codex` | GPT-5.2 Codex | chat | active | text |
| `chatgpt-image-latest` | ChatGPT Image Latest | image | active | text, image |
| `gpt-4o-mini-tts-2025-12-15` | GPT-4o Mini TTS | audio | active | text |
| `gpt-4o-mini-transcribe-2025-12-15` | GPT-4o Mini Transcribe | audio | active | audio |
| `gpt-5.2-chat-latest` | GPT-5.2 Chat Latest | chat | active | text |
| `gpt-5.2-pro` | GPT-5.2 Pro | chat | active | text |
| `gpt-5.2` | GPT-5.2 | chat | active | text |
| `gpt-5.1-codex-max` | GPT-5.1 Codex Max | chat | active | text |
| `gpt-5.1-codex` | GPT-5.1 Codex | chat | active | text |
| `gpt-5.1` | GPT-5.1 | chat | active | text |
| `gpt-5.1-chat-latest` | GPT-5.1 Chat Latest | chat | active | text |
| `gpt-5-search-api` | GPT-5 Search API | chat | active | text |
| `gpt-5-pro` | GPT-5 Pro | chat | active | text |
| `gpt-5-codex` | GPT-5 Codex | chat | active | text |
| `gpt-5-nano` | GPT-5 Nano | chat | active | text |
| `gpt-5-mini` | GPT-5 Mini | chat | active | text |
| `gpt-5` | GPT-5 | chat | active | text |
| `gpt-5-chat-latest` | GPT-5 Chat Latest | chat | active | text |
| `o4-mini-deep-research` | o4 Mini Deep Research | reasoning | active | text |
| `gpt-4o-audio-preview-2025-06-03` | GPT-4o Audio Preview | audio | preview | text, audio |
| `gpt-4o-realtime-preview-2025-06-03` | GPT-4o Realtime Preview | audio | preview | text, audio |
| `gpt-4.1` | GPT-4.1 | chat | active | text |
| `o4-mini` | o4 Mini | reasoning | active | text |
| `o3` | o3 | reasoning | active | text |
| `o1-pro` | o1 Pro | reasoning | active | text |
| `gpt-4o-mini-search-preview` | GPT-4o Mini Search Preview | chat | preview | text, image |
| `gpt-4o-search-preview` | GPT-4o Search Preview | chat | preview | text, image |
| `o3-mini` | o3 Mini | reasoning | active | text |
| `gpt-4o-mini-audio-preview` | GPT-4o Mini Audio Preview | audio | preview | text, image, audio |
| `gpt-4o-mini-realtime-preview` | GPT-4o Mini Realtime Preview | audio | preview | text, image, audio |
| `o1` | o1 | reasoning | active | text |
| `gpt-4o-realtime-preview` | GPT-4o Realtime Preview | audio | preview | text, image, audio |
| `gpt-4o-audio-preview` | GPT-4o Audio Preview | audio | preview | text, image, audio |
| `chatgpt-4o-latest` | ChatGPT-4o Latest | chat | active | text, image |
| `gpt-4o-mini` | GPT-4o Mini | chat | active | text, image |
| `gpt-4o` | GPT-4o | chat | active | text, image |
| `gpt-4-turbo` | GPT-4 Turbo | chat | active | text |
| `gpt-4` | GPT-4 | chat | active | text |
| `gpt-3.5-turbo` | GPT-3.5 Turbo | chat | active | text |

## Anthropic

**Provider:** Anthropic | [Website](https://anthropic.com) | [API Docs](https://docs.anthropic.com)

| Model ID | Name | Type | Status | Input Modalities |
|----------|------|------|--------|------------------|
| `claude-opus-4-5-20251101` | Claude Opus 4.5 | chat | active | text |
| `claude-haiku-4-5-20251001` | Claude Haiku 4.5 | chat | active | text |
| `claude-sonnet-4-5-20250929` | Claude Sonnet 4.5 | chat | active | text |
| `claude-opus-4-1-20250805` | Claude Opus 4.1 | chat | active | text |
| `claude-opus-4-20250514` | Claude Opus 4 | chat | active | text |
| `claude-sonnet-4-20250514` | Claude Sonnet 4 | chat | active | text |
| `claude-3-5-haiku-20241022` | Claude Haiku 3.5 | chat | active | text |
| `claude-3-haiku-20240307` | Claude Haiku 3 | chat | active | text |

## Google

**Provider:** Google | [Website](https://ai.google.dev) | [API Docs](https://ai.google.dev/docs)

| Model ID | Name | Type | Status | Input Modalities | Context Window |
|----------|------|------|--------|------------------|----------------|
| `models/gemini-3-pro-preview` | Gemini 3 Pro Preview | chat | preview | text | 1M |
| `models/gemini-3-flash-preview` | Gemini 3 Flash Preview | chat | preview | text | 1M |
| `models/gemini-3-pro-image-preview` | Gemini 3 Pro Image Preview | chat | preview | text, image | 131K |
| `models/gemini-2.5-flash` | Gemini 2.5 Flash | chat | active | text | 1M |
| `models/gemini-2.5-pro` | Gemini 2.5 Pro | chat | active | text | 1M |
| `models/gemini-2.5-flash-lite` | Gemini 2.5 Flash-Lite | chat | active | text | 1M |
| `models/gemini-2.0-flash` | Gemini 2.0 Flash | chat | active | text | 1M |
| `models/gemini-2.0-flash-lite` | Gemini 2.0 Flash-Lite | chat | active | text | 1M |

---

**Note:** Preview models may have limited availability or experimental features. Context window is shown in tokens (K = thousands, M = millions) where available.