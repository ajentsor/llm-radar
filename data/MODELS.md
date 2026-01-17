# AI Models Reference

**Last Updated:** January 17, 2026

**Summary:** 85 OpenAI models including GPT-5.2, GPT-5.1, GPT-5, o-series reasoning models, and GPT-4o variants; 8 Anthropic Claude models from 3.0 to 4.5; 31 Google Gemini models including 2.0, 2.5, and 3.0 variants with multimodal capabilities.

## OpenAI

[Documentation](https://platform.openai.com/docs) | [Website](https://openai.com)

| Model ID | Type | Status | Input Support |
|----------|------|--------|---------------|
| `gpt-5.2-codex` | chat | active | text |
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
| `gpt-4.1` | chat | active | text |
| `chatgpt-4o-latest` | chat | active | text, image |
| `gpt-4o-mini` | chat | active | text, image |
| `gpt-4o` | chat | active | text, image |
| `gpt-4-turbo` | chat | active | text |
| `gpt-4` | chat | active | text |
| `gpt-3.5-turbo` | chat | active | text |
| `gpt-4o-mini-search-preview` | chat | preview | text |
| `gpt-4o-search-preview` | chat | preview | text |
| `o4-mini-deep-research` | reasoning | active | text |
| `o4-mini` | reasoning | active | text |
| `o3` | reasoning | active | text |
| `o3-mini` | reasoning | active | text |
| `o1-pro` | reasoning | active | text |
| `o1` | reasoning | active | text |
| `chatgpt-image-latest` | image | active | text |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio |
| `gpt-4o-realtime-preview` | audio | preview | text, audio |
| `gpt-4o-audio-preview` | audio | preview | text, audio |

## Anthropic

[Documentation](https://docs.anthropic.com) | [Website](https://anthropic.com)

| Model ID | Type | Status | Input Support |
|----------|------|--------|---------------|
| `claude-opus-4-5-20251101` | chat | active | text |
| `claude-haiku-4-5-20251001` | chat | active | text |
| `claude-sonnet-4-5-20250929` | chat | active | text |
| `claude-opus-4-1-20250805` | chat | active | text |
| `claude-opus-4-20250514` | chat | active | text |
| `claude-sonnet-4-20250514` | chat | active | text |
| `claude-3-5-haiku-20241022` | chat | active | text |
| `claude-3-haiku-20240307` | chat | active | text |

## Google

[Documentation](https://ai.google.dev/docs) | [Website](https://ai.google.dev)

| Model ID | Type | Status | Input Support |
|----------|------|--------|---------------|
| `models/gemini-3-pro-preview` | chat | preview | text |
| `models/gemini-3-flash-preview` | chat | preview | text |
| `models/gemini-2.5-flash` | chat | active | text |
| `models/gemini-2.5-pro` | chat | active | text |
| `models/gemini-2.0-flash` | chat | active | text |

## Notes

- **Preview models** may have limited availability or stability
- **Multimodal models** support additional input types beyond text (images, audio)
- Model IDs should be used exactly as shown for API calls
- Context windows and specific capabilities may vary - refer to provider documentation