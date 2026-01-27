# AI Models Reference

**Last Updated:** January 27, 2026

**Summary:** 85 OpenAI models including GPT-5.2, GPT-5.1, GPT-5, O-series reasoning models, and audio capabilities; 8 Anthropic Claude models up to version 4.5; 31 Google Gemini models including 3.0 preview and 2.5 versions.

## OpenAI

**Documentation:** https://platform.openai.com/docs  
**API Base:** https://api.openai.com

| Model ID | Type | Status | Input Modalities |
|----------|------|--------|------------------|
| `gpt-5.2-codex` | chat | active | text |
| `chatgpt-image-latest` | image | active | text |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio |
| `gpt-5.2-chat-latest` | chat | active | text |
| `gpt-5.2-pro` | chat | active | text |
| `gpt-5.2` | chat | active | text |
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
| `chatgpt-4o-latest` | chat | active | text, image |
| `gpt-4o-mini` | chat | active | text, image |
| `gpt-4o` | chat | active | text, image |
| `gpt-4-turbo` | chat | active | text |
| `gpt-4` | chat | active | text |
| `gpt-3.5-turbo` | chat | active | text |

## Anthropic

**Documentation:** https://docs.anthropic.com  
**API Base:** https://api.anthropic.com

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

**Documentation:** https://ai.google.dev/docs  
**API Base:** https://generativelanguage.googleapis.com

| Model ID | Type | Status | Input Modalities | Context Window |
|----------|------|--------|------------------|----------------|
| `models/gemini-3-pro-preview` | chat | preview | text | 1,048,576 |
| `models/gemini-3-flash-preview` | chat | preview | text | 1,048,576 |
| `models/gemini-3-pro-image-preview` | chat | preview | text, image | 131,072 |
| `models/gemini-2.5-flash` | chat | active | text | 1,048,576 |
| `models/gemini-2.5-pro` | chat | active | text | 1,048,576 |
| `models/gemini-2.5-flash-lite` | chat | active | text | 1,048,576 |
| `models/gemini-2.0-flash` | chat | active | text | 1,048,576 |
| `models/gemini-2.0-flash-lite` | chat | active | text | 1,048,576 |

## Model Types

- **chat**: Text-to-text conversation models
- **reasoning**: Advanced reasoning and problem-solving models
- **audio**: Speech/audio processing (TTS, STT, realtime)
- **image**: Image generation models

## Status Indicators

- **active**: Generally available for production use
- **preview**: Early access, may have limitations or changes