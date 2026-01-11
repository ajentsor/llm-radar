# AI Models Reference

**Last Updated:** January 11, 2026  
**Summary:** 84 OpenAI models including GPT-5.2, GPT-5.1, O-series reasoning models, and GPT-4 variants; 8 Anthropic Claude models up to version 4.5; 32 Google Gemini models including 3.0, 2.5, and 2.0 versions.

## OpenAI

**Website:** https://openai.com  
**API Documentation:** https://platform.openai.com/docs

| Model ID | Type | Status | Multimodal |
|----------|------|---------|-----------|
| `chatgpt-image-latest` | image | active | ✓ (text, image) |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | ✓ (text → audio) |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | ✓ (audio → text) |
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
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | ✓ (text, audio) |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | ✓ (text, audio) |
| `gpt-4.1` | chat | active | |
| `o4-mini` | reasoning | active | |
| `o3` | reasoning | active | |
| `o1-pro` | reasoning | active | |
| `gpt-4o-mini-search-preview` | chat | preview | |
| `gpt-4o-search-preview` | chat | preview | |
| `o3-mini` | reasoning | active | |
| `gpt-4o-mini-audio-preview` | audio | preview | ✓ (text, audio) |
| `gpt-4o-mini-realtime-preview` | audio | preview | ✓ (text, audio) |
| `o1` | reasoning | active | |
| `gpt-4o-realtime-preview` | audio | preview | ✓ (text, audio) |
| `gpt-4o-audio-preview` | audio | preview | ✓ (text, audio) |
| `chatgpt-4o-latest` | chat | active | ✓ (text, image) |
| `gpt-4o-mini` | chat | active | ✓ (text, image) |
| `gpt-4o` | chat | active | ✓ (text, image) |
| `gpt-4-turbo` | chat | active | |
| `gpt-4` | chat | active | |
| `gpt-3.5-turbo` | chat | active | |

## Anthropic

**Website:** https://anthropic.com  
**API Documentation:** https://docs.anthropic.com

| Model ID | Type | Status | Multimodal |
|----------|------|---------|-----------|
| `claude-opus-4-5-20251101` | chat | active | |
| `claude-haiku-4-5-20251001` | chat | active | |
| `claude-sonnet-4-5-20250929` | chat | active | |
| `claude-opus-4-1-20250805` | chat | active | |
| `claude-opus-4-20250514` | chat | active | |
| `claude-sonnet-4-20250514` | chat | active | |
| `claude-3-5-haiku-20241022` | chat | active | |
| `claude-3-haiku-20240307` | chat | active | |

## Google

**Website:** https://ai.google  
**API Documentation:** https://ai.google.dev/docs

| Model ID | Type | Status | Context Window | Multimodal |
|----------|------|---------|----------------|-----------|
| `models/gemini-3-pro-preview` | chat | preview | 1,048,576 | |
| `models/gemini-3-flash-preview` | chat | preview | 1,048,576 | |
| `models/gemini-2.5-flash` | chat | active | 1,048,576 | |
| `models/gemini-2.5-pro` | chat | active | 1,048,576 | |
| `models/gemini-2.5-flash-preview-tts` | audio | preview | 8,192 | ✓ (text → audio) |
| `models/gemini-2.5-pro-preview-tts` | audio | preview | 8,192 | ✓ (text → audio) |
| `models/gemini-2.5-flash-lite` | chat | active | 1,048,576 | |
| `models/gemini-2.0-flash` | chat | active | 1,048,576 | |
| `models/gemini-2.0-flash-lite` | chat | active | 1,048,576 | |

---

**Legend:**
- **Type:** Model capability (chat, reasoning, audio, image)
- **Status:** active (production-ready), preview (experimental)  
- **Multimodal:** Indicates support for non-text inputs/outputs