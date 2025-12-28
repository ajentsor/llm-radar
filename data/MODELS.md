# AI Models Reference

**Last Updated:** December 28, 2025  
**Summary:** 84 OpenAI models including GPT-5.2, GPT-5.1, O-series reasoning models, and GPT-4o variants; 8 Anthropic Claude models up to version 4.5; 32 Google Gemini models including 3.0 preview and 2.5 versions.

## OpenAI

**Provider:** [OpenAI](https://openai.com) | **API Docs:** [platform.openai.com/docs](https://platform.openai.com/docs)

| Model ID | Type | Status | Input Modalities |
|----------|------|--------|------------------|
| `chatgpt-image-latest` | image | active | text |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio |
| `gpt-5.2-chat-latest` | chat | active | text |
| `gpt-5.2-pro` | chat | active | text |
| `gpt-5.2` | chat | active | text |
| `gpt-5.1-codex-max` | chat | active | text |
| `gpt-5.1-codex-mini` | chat | active | text |
| `gpt-5.1-codex` | chat | active | text |
| `gpt-5.1` | chat | active | text |
| `gpt-5.1-chat-latest` | chat | active | text |
| `gpt-5-search-api` | chat | active | text |
| `gpt-5-pro` | chat | active | text |
| `gpt-5-codex` | chat | active | text |
| `gpt-5-nano` | chat | active | text |
| `gpt-5-mini` | chat | active | text |
| `gpt-5` | chat | active | text |
| `gpt-5-chat-latest` | chat | active | text |
| `o4-mini-deep-research` | reasoning | active | text |
| `gpt-4o-transcribe-diarize` | audio | active | audio |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio |
| `gpt-4.1-nano` | chat | active | text |
| `gpt-4.1-mini` | chat | active | text |
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

**Provider:** [Anthropic](https://anthropic.com) | **API Docs:** [docs.anthropic.com](https://docs.anthropic.com)

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

**Provider:** [Google](https://cloud.google.com) | **API Docs:** [cloud.google.com/vertex-ai/docs](https://cloud.google.com/vertex-ai/docs)

| Model ID | Type | Status | Input Modalities |
|----------|------|--------|------------------|
| `gemini-3-pro-preview` | chat | preview | text |
| `gemini-3-flash-preview` | chat | preview | text |
| `gemini-2.5-flash` | chat | active | text |
| `gemini-2.5-pro` | chat | active | text |
| `gemini-2.5-flash-lite` | chat | active | text |
| `gemini-2.0-flash` | chat | active | text |
| `gemini-2.0-flash-lite` | chat | active | text |

## Notes

- **Multimodal Models:** Models supporting image/audio input are indicated in the Input Modalities column
- **Status:** `active` = production ready, `preview` = experimental/beta
- **Model Types:** `chat` = conversational, `reasoning` = advanced problem-solving, `audio` = speech/transcription, `image` = image generation
- **Context Window:** Most models support extended context (up to 1M+ tokens for Gemini models)