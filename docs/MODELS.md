# AI Models Reference

**Last Updated:** January 20, 2026  
**Summary:** 85 OpenAI models, 8 Anthropic models, and 31 Google Gemini models are currently accessible via API, including advanced GPT-5 series, Claude 4.5 models, and Gemini 3.0 preview models.

## OpenAI

[API Documentation](https://platform.openai.com/docs) | [Website](https://openai.com)

| Model ID | Type | Status | Modalities |
|----------|------|--------|------------|
| `gpt-5.2-codex` | chat | active | text → text |
| `chatgpt-image-latest` | image | active | text → image |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text → audio |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio → text |
| `gpt-5.2-chat-latest` | chat | active | text → text |
| `gpt-5.2-pro` | chat | active | text → text |
| `gpt-5.2` | chat | active | text → text |
| `gpt-5.1-codex-max` | chat | active | text → text |
| `gpt-5.1-codex` | chat | active | text → text |
| `gpt-5.1` | chat | active | text → text |
| `gpt-5.1-chat-latest` | chat | active | text → text |
| `gpt-5-search-api` | chat | active | text → text |
| `gpt-5-pro` | chat | active | text → text |
| `gpt-5-codex` | chat | active | text → text |
| `gpt-5-nano` | chat | active | text → text |
| `gpt-5-mini` | chat | active | text → text |
| `gpt-5` | chat | active | text → text |
| `gpt-5-chat-latest` | chat | active | text → text |
| `o4-mini-deep-research` | reasoning | active | text → text |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio → text, audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio → text, audio |
| `gpt-4.1` | chat | active | text → text |
| `o4-mini` | reasoning | active | text → text |
| `o3` | reasoning | active | text → text |
| `o1-pro` | reasoning | active | text → text |
| `gpt-4o-mini-search-preview` | chat | preview | text, image → text |
| `gpt-4o-search-preview` | chat | preview | text, image → text |
| `o3-mini` | reasoning | active | text → text |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio → text, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio → text, audio |
| `o1` | reasoning | active | text → text |
| `gpt-4o-realtime-preview` | audio | preview | text, audio → text, audio |
| `gpt-4o-audio-preview` | audio | preview | text, audio → text, audio |
| `chatgpt-4o-latest` | chat | active | text, image → text |
| `gpt-4o-mini` | chat | active | text, image → text |
| `gpt-4o` | chat | active | text, image → text |
| `gpt-4-turbo` | chat | active | text → text |
| `gpt-4` | chat | active | text → text |
| `gpt-3.5-turbo` | chat | active | text → text |

## Anthropic

[API Documentation](https://docs.anthropic.com) | [Website](https://anthropic.com)

| Model ID | Type | Status | Modalities |
|----------|------|--------|------------|
| `claude-opus-4-5-20251101` | chat | active | text → text |
| `claude-haiku-4-5-20251001` | chat | active | text → text |
| `claude-sonnet-4-5-20250929` | chat | active | text → text |
| `claude-opus-4-1-20250805` | chat | active | text → text |
| `claude-opus-4-20250514` | chat | active | text → text |
| `claude-sonnet-4-20250514` | chat | active | text → text |
| `claude-3-5-haiku-20241022` | chat | active | text → text |
| `claude-3-haiku-20240307` | chat | active | text → text |

## Google

[API Documentation](https://ai.google.dev/docs) | [Website](https://ai.google.dev)

| Model ID | Type | Status | Context Window | Modalities |
|----------|------|--------|----------------|------------|
| `models/gemini-3-pro-preview` | chat | preview | 1M tokens | text → text |
| `models/gemini-3-flash-preview` | chat | preview | 1M tokens | text → text |
| `models/gemini-2.5-flash` | chat | active | 1M tokens | text → text |
| `models/gemini-2.5-pro` | chat | active | 1M tokens | text → text |
| `models/gemini-2.0-flash-exp` | chat | preview | 1M tokens | text → text |
| `models/gemini-2.0-flash` | chat | active | 1M tokens | text → text |

## Notes

- **Multimodal Support**: Models marked with multiple input modalities (text, image, audio) support multimodal inputs
- **Preview/Experimental**: Models with preview or experimental status may have limited availability or different API endpoints
- **Context Windows**: Only specified where available in the source data
- **Model Types**: 
  - `chat`: Text generation and conversation
  - `audio`: Audio processing (TTS, transcription, real-time)
  - `image`: Image generation
  - `reasoning`: Advanced reasoning capabilities