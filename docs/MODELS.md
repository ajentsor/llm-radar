# Available AI Models

**Last Updated:** January 16, 2026

**Summary:** 85 OpenAI models including GPT-5.2 series and O-series reasoning models, 8 Anthropic Claude models through version 4.5, and 31 Google Gemini models including 3.0 preview versions are accessible via API.

## Quick Reference

### OpenAI Models
| Model ID | Type | Status | Multimodal |
|----------|------|--------|------------|
| `gpt-5.2-codex` | chat | active | |
| `chatgpt-image-latest` | image | active | |
| `gpt-4o-mini-tts-2025-12-15` | audio | active | |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio → text |
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
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text + audio |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text + audio |
| `gpt-4.1` | chat | active | |
| `o4-mini` | reasoning | active | |
| `o3` | reasoning | active | |
| `o1-pro` | reasoning | active | |
| `gpt-4o-mini-search-preview` | chat | preview | |
| `gpt-4o-search-preview` | chat | preview | |
| `o3-mini` | reasoning | active | |
| `gpt-4o-mini-audio-preview` | audio | preview | text + audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text + audio |
| `o1` | reasoning | active | |
| `gpt-4o-realtime-preview` | audio | preview | text + audio |
| `gpt-4o-audio-preview` | audio | preview | text + audio |
| `chatgpt-4o-latest` | chat | active | text + image |
| `gpt-4o-mini` | chat | active | text + image |
| `gpt-4o` | chat | active | text + image |
| `gpt-4-turbo` | chat | active | |
| `gpt-4` | chat | active | |
| `gpt-3.5-turbo` | chat | active | |

**Documentation:** [OpenAI API Docs](https://platform.openai.com/docs)

### Anthropic Claude Models
| Model ID | Type | Status | Multimodal |
|----------|------|--------|------------|
| `claude-opus-4-5-20251101` | chat | active | |
| `claude-haiku-4-5-20251001` | chat | active | |
| `claude-sonnet-4-5-20250929` | chat | active | |
| `claude-opus-4-1-20250805` | chat | active | |
| `claude-opus-4-20250514` | chat | active | |
| `claude-sonnet-4-20250514` | chat | active | |
| `claude-3-5-haiku-20241022` | chat | active | |
| `claude-3-haiku-20240307` | chat | active | |

**Documentation:** [Anthropic API Docs](https://docs.anthropic.com)

### Google Gemini Models
| Model ID | Type | Status | Multimodal | Context Window |
|----------|------|--------|------------|----------------|
| `models/gemini-3-pro-preview` | chat | preview | | 1M tokens |
| `models/gemini-3-flash-preview` | chat | preview | | 1M tokens |
| `models/gemini-2.5-flash` | chat | active | | 1M tokens |
| `models/gemini-2.5-pro` | chat | active | | 1M tokens |
| `models/gemini-2.5-flash-preview-tts` | audio | preview | text → audio | 8K tokens |
| `models/gemini-2.5-flash-lite` | chat | active | | 1M tokens |
| `models/gemini-2.5-computer-use-preview-10-2025` | chat | preview | | 131K tokens |
| `models/gemini-2.5-flash-native-audio-latest` | audio | active | text + audio | 131K tokens |
| `models/gemini-2.0-flash-exp` | chat | preview | | 1M tokens |
| `models/gemini-2.0-flash` | chat | active | | 1M tokens |
| `models/gemini-2.0-flash-lite` | chat | active | | 1M tokens |

**Documentation:** [Google Vertex AI Docs](https://cloud.google.com/vertex-ai/docs)

## Model Types

- **chat**: Text generation and conversation
- **reasoning**: Advanced problem-solving with step-by-step thinking
- **audio**: Speech-to-text, text-to-speech, or audio conversation
- **image**: Image generation

## Status Types

- **active**: Generally available for production use
- **preview**: Early access, may have limitations or changes