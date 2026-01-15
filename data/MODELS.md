# AI Models Reference

**Last Updated:** January 15, 2026  
**Summary:** 125 models across 3 providers - 85 OpenAI models (GPT-5.2, GPT-4o, o-series), 8 Anthropic Claude models (up to Claude Opus 4.5), 32 Google Gemini models (Gemini 3 Pro, 2.5 variants)

## OpenAI Models

**Provider:** [OpenAI](https://openai.com) | **API Docs:** [platform.openai.com/docs](https://platform.openai.com/docs)

| Model ID | Type | Status | Input Modalities |
|----------|------|--------|------------------|
| `gpt-5.2-codex` | chat | active | text |
| `chatgpt-image-latest` | image | active | text |
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
| `gpt-4o-mini-search-preview` | chat | preview | text |
| `gpt-4o-search-preview` | chat | preview | text |
| `o3-mini` | reasoning | active | text |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio |
| `o1` | reasoning | active | text |
| `gpt-4o-realtime-preview` | audio | preview | text, audio |
| `gpt-4o-audio-preview` | audio | preview | text, audio |
| `chatgpt-4o-latest` | chat | active | text |
| `gpt-4o-mini` | chat | active | text, image |
| `gpt-4o` | chat | active | text, image |
| `gpt-4-turbo` | chat | active | text |
| `gpt-4` | chat | active | text |
| `gpt-3.5-turbo` | chat | active | text |

## Anthropic Models

**Provider:** [Anthropic](https://anthropic.com) | **API Docs:** [docs.anthropic.com/claude/reference](https://docs.anthropic.com/claude/reference)

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

**Provider:** [Google](https://ai.google.dev) | **API Docs:** [ai.google.dev/docs](https://ai.google.dev/docs)

| Model ID | Type | Status | Context Window | Input Modalities |
|----------|------|--------|----------------|------------------|
| `models/gemini-3-pro-preview` | chat | preview | 1M | text |
| `models/gemini-3-flash-preview` | chat | preview | 1M | text |
| `models/gemini-2.5-flash` | chat | active | 1M | text |
| `models/gemini-2.5-pro` | chat | active | 1M | text |
| `models/gemini-2.5-flash-preview-tts` | audio | preview | 8K | text |
| `models/gemini-2.5-pro-preview-tts` | audio | preview | 8K | text |
| `models/gemini-2.5-flash-lite` | chat | active | 1M | text |
| `models/gemini-2.5-computer-use-preview-10-2025` | chat | preview | 128K | text |
| `models/gemini-2.5-flash-native-audio-latest` | audio | active | 128K | audio |
| `models/gemini-2.0-flash-exp` | chat | experimental | 1M | text |
| `models/gemini-2.0-flash` | chat | active | 1M | text |

## Notes

- **Multimodal Support:** Models with image/audio input capabilities are marked in the Input Modalities column
- **Context Windows:** K = thousand tokens, M = million tokens
- **Status Definitions:**
  - `active` - Production ready
  - `preview` - Available for testing, may have limitations
  - `experimental` - Early access, subject to changes