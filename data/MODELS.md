# AI Models Reference

**Last Updated:** January 1, 2026  
**Summary:** 84 OpenAI models including GPT-5.2, GPT-5.1, o4-mini, o3-mini and o1 series; 8 Anthropic Claude models up to version 4.5; 32 Google Gemini models including 3.0 preview and 2.5 series available via API.

## OpenAI

**API Documentation:** https://platform.openai.com/docs

| Model ID | Type | Status | Multimodal |
|----------|------|--------|------------|
| `chatgpt-image-latest` | image | active | text→image |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text→audio |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio→text |
| `gpt-5.2-chat-latest` | chat | active | - |
| `gpt-5.2-pro` | chat | active | - |
| `gpt-5.2` | chat | active | - |
| `gpt-5.1-codex-max` | chat | active | - |
| `gpt-5.1-codex` | chat | active | - |
| `gpt-5.1` | chat | active | - |
| `gpt-5.1-chat-latest` | chat | active | - |
| `gpt-5-search-api` | chat | active | - |
| `gpt-5-pro` | chat | active | - |
| `gpt-5-codex` | chat | active | - |
| `gpt-5` | chat | active | - |
| `gpt-5-chat-latest` | chat | active | - |
| `o4-mini-deep-research` | reasoning | active | - |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text+audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text+audio |
| `gpt-4.1` | chat | active | - |
| `o4-mini` | reasoning | active | - |
| `o3` | reasoning | active | - |
| `o1-pro` | reasoning | active | - |
| `gpt-4o-mini-search-preview` | chat | preview | text+image |
| `gpt-4o-search-preview` | chat | preview | text+image |
| `o3-mini` | reasoning | active | - |
| `gpt-4o-mini-audio-preview` | audio | preview | text+audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text+audio |
| `o1` | reasoning | active | - |
| `gpt-4o-audio-preview` | audio | preview | text+audio |
| `gpt-4o-realtime-preview` | audio | preview | text+audio |
| `chatgpt-4o-latest` | chat | active | text+image |
| `gpt-4o-mini` | chat | active | text+image |
| `gpt-4o` | chat | active | text+image |
| `gpt-4-turbo` | chat | active | - |
| `gpt-4` | chat | active | - |
| `gpt-3.5-turbo` | chat | active | - |

## Anthropic

**API Documentation:** https://docs.anthropic.com

| Model ID | Type | Status | Multimodal |
|----------|------|--------|------------|
| `claude-opus-4-5-20251101` | chat | active | - |
| `claude-haiku-4-5-20251001` | chat | active | - |
| `claude-sonnet-4-5-20250929` | chat | active | - |
| `claude-opus-4-1-20250805` | chat | active | - |
| `claude-opus-4-20250514` | chat | active | - |
| `claude-sonnet-4-20250514` | chat | active | - |
| `claude-3-5-haiku-20241022` | chat | active | - |
| `claude-3-haiku-20240307` | chat | active | - |

## Google

**API Documentation:** https://ai.google.dev/docs

| Model ID | Type | Status | Multimodal |
|----------|------|--------|------------|
| `gemini-3-pro-preview` | chat | preview | - |
| `gemini-3-flash-preview` | chat | preview | - |
| `gemini-2.5-flash` | chat | active | - |
| `gemini-2.5-pro` | chat | active | - |
| `gemini-2.5-flash-preview-tts` | audio | preview | text→audio |
| `gemini-2.0-flash` | chat | active | - |

---

**Note:** Model IDs shown above are the exact strings to use in API calls. Multimodal capabilities are indicated where supported (text+image, text+audio, etc.).