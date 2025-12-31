# AI Models API Reference

**Last Updated:** December 31, 2025  
**Summary:** 84 OpenAI models, 8 Anthropic models, and 32 Google Gemini models are accessible via API, including latest GPT-5.2, Claude 4.5, and Gemini 3 series.

## OpenAI Models

[API Documentation](https://platform.openai.com/docs) | [Website](https://openai.com)

| Model ID | Type | Status | Input | Output |
|----------|------|--------|-------|--------|
| `chatgpt-image-latest` | image | active | text, image | text |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text | audio |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio | text |
| `gpt-5.2-chat-latest` | chat | active | text | text |
| `gpt-5.2-pro` | chat | active | text | text |
| `gpt-5.2` | chat | active | text | text |
| `gpt-5.1-codex-max` | chat | active | text | text |
| `gpt-5.1-codex` | chat | active | text | text |
| `gpt-5.1` | chat | active | text | text |
| `gpt-5.1-chat-latest` | chat | active | text | text |
| `gpt-5-search-api` | chat | active | text | text |
| `gpt-5-pro` | chat | active | text | text |
| `gpt-5-codex` | chat | active | text | text |
| `gpt-5` | chat | active | text | text |
| `gpt-5-chat-latest` | chat | active | text | text |
| `o4-mini-deep-research` | reasoning | active | text | text |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio | text, audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio | text, audio |
| `gpt-4.1` | chat | active | text | text |
| `o4-mini` | reasoning | active | text | text |
| `o3` | reasoning | active | text | text |
| `o1-pro` | reasoning | active | text | text |
| `gpt-4o-mini-search-preview` | chat | preview | text | text |
| `gpt-4o-search-preview` | chat | preview | text | text |
| `o3-mini` | reasoning | active | text | text |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio | text, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio | text, audio |
| `o1` | reasoning | active | text | text |
| `gpt-4o-audio-preview` | audio | preview | text, audio | text, audio |
| `gpt-4o-realtime-preview` | audio | preview | text, audio | text, audio |
| `chatgpt-4o-latest` | chat | active | text, image | text |
| `gpt-4o-mini` | chat | active | text, image | text |
| `gpt-4o` | chat | active | text, image | text |
| `gpt-4-turbo` | chat | active | text | text |
| `gpt-4` | chat | active | text | text |
| `gpt-3.5-turbo` | chat | active | text | text |

## Anthropic Models

[API Documentation](https://docs.anthropic.com) | [Website](https://anthropic.com)

| Model ID | Type | Status | Input | Output |
|----------|------|--------|-------|--------|
| `claude-opus-4-5-20251101` | chat | active | text | text |
| `claude-haiku-4-5-20251001` | chat | active | text | text |
| `claude-sonnet-4-5-20250929` | chat | active | text | text |
| `claude-opus-4-1-20250805` | chat | active | text | text |
| `claude-opus-4-20250514` | chat | active | text | text |
| `claude-sonnet-4-20250514` | chat | active | text | text |
| `claude-3-5-haiku-20241022` | chat | active | text | text |
| `claude-3-haiku-20240307` | chat | active | text | text |

## Google Models

[API Documentation](https://ai.google.dev/docs) | [Website](https://ai.google.dev)

| Model ID | Type | Status | Input | Output | Context Window |
|----------|------|--------|-------|--------|----------------|
| `gemini-3-pro-preview` | chat | preview | text | text | 1M |
| `gemini-3-flash-preview` | chat | preview | text | text | 1M |
| `gemini-2.5-flash` | chat | active | text | text | 1M |
| `gemini-2.5-pro` | chat | active | text | text | 1M |
| `gemini-2.5-flash-preview-tts` | audio | preview | text | audio | 8K |
| `gemini-2.0-flash` | chat | active | text | text | 1M |

## Notes

- **Multimodal Models**: Models with image/audio input capabilities are marked in the Input column
- **Preview Status**: Preview models may have limited availability or experimental features
- **Context Windows**: Listed where available (K = thousand tokens, M = million tokens)
- **Model IDs**: Use exact strings from Model ID column in API calls