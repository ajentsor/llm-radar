# Available AI Models

**Last Updated:** 2026-01-26 08:32 UTC

**Summary:** 85 OpenAI models including GPT-5.2, GPT-5.1, GPT-5, O-series reasoning models, and GPT-4 variants; 8 Anthropic Claude models up to Claude Opus 4.5; 31 Google Gemini models including Gemini 3 Pro Preview and Gemini 2.5 series.

## OpenAI

**Documentation:** [platform.openai.com/docs](https://platform.openai.com/docs)

### Chat Models

| Model ID | Type | Status | Input | Notes |
|----------|------|--------|-------|-------|
| `gpt-5.2-codex` | chat | active | text | Code-focused |
| `gpt-5.2-chat-latest` | chat | active | text | Latest version |
| `gpt-5.2-pro` | chat | active | text | Professional version |
| `gpt-5.2` | chat | active | text | Base model |
| `gpt-5.1-codex` | chat | active | text | Code-focused |
| `gpt-5.1` | chat | active | text | Base model |
| `gpt-5.1-chat-latest` | chat | active | text | Latest version |
| `gpt-5-search-api` | chat | active | text | Search capabilities |
| `gpt-5-pro` | chat | active | text | Professional version |
| `gpt-5-codex` | chat | active | text | Code-focused |
| `gpt-5-nano` | chat | active | text | Compact version |
| `gpt-5-mini` | chat | active | text | Smaller version |
| `gpt-5` | chat | active | text | Base model |
| `gpt-5-chat-latest` | chat | active | text | Latest version |
| `gpt-4.1` | chat | active | text | |
| `chatgpt-4o-latest` | chat | active | text, image | Latest ChatGPT |
| `gpt-4o-mini` | chat | active | text, image | Smaller version |
| `gpt-4o` | chat | active | text, image | Enhanced capabilities |
| `gpt-4-turbo` | chat | active | text | Faster version |
| `gpt-4` | chat | active | text | Base model |
| `gpt-3.5-turbo` | chat | active | text | Chat optimized |
| `gpt-4o-mini-search-preview` | chat | preview | text | Search capabilities |
| `gpt-4o-search-preview` | chat | preview | text | Search capabilities |

### Reasoning Models

| Model ID | Type | Status | Input | Notes |
|----------|------|--------|-------|-------|
| `o4-mini-deep-research` | reasoning | active | text | Research-focused |
| `o4-mini` | reasoning | active | text | Smaller version |
| `o3` | reasoning | active | text | |
| `o1-pro` | reasoning | active | text | Professional version |
| `o3-mini` | reasoning | active | text | Smaller version |
| `o1` | reasoning | active | text | |

### Audio Models

| Model ID | Type | Status | Input | Output | Notes |
|----------|------|--------|-------|--------|-------|
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text | audio | Text-to-speech |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio | text | Transcription |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio | text, audio | |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio | text, audio | Real-time |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio | text, audio | |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio | text, audio | Real-time |
| `gpt-4o-realtime-preview` | audio | preview | text, audio | text, audio | Real-time |
| `gpt-4o-audio-preview` | audio | preview | text, audio | text, audio | |

### Image Models

| Model ID | Type | Status | Input | Output | Notes |
|----------|------|--------|-------|--------|-------|
| `chatgpt-image-latest` | image | active | text | image | Latest generation |

## Anthropic

**Documentation:** [docs.anthropic.com](https://docs.anthropic.com)

| Model ID | Type | Status | Input | Notes |
|----------|------|--------|-------|-------|
| `claude-opus-4-5-20251101` | chat | active | text | Opus 4.5 |
| `claude-haiku-4-5-20251001` | chat | active | text | Haiku 4.5 |
| `claude-sonnet-4-5-20250929` | chat | active | text | Sonnet 4.5 |
| `claude-opus-4-1-20250805` | chat | active | text | Opus 4.1 |
| `claude-opus-4-20250514` | chat | active | text | Opus 4 |
| `claude-sonnet-4-20250514` | chat | active | text | Sonnet 4 |
| `claude-3-5-haiku-20241022` | chat | active | text | Haiku 3.5 |
| `claude-3-haiku-20240307` | chat | active | text | Haiku 3 |

## Google

**Documentation:** [ai.google.dev/docs](https://ai.google.dev/docs)

| Model ID | Type | Status | Input | Context Window | Notes |
|----------|------|--------|-------|----------------|-------|
| `models/gemini-3-pro-preview` | chat | preview | text | 1M tokens | Preview |
| `models/gemini-3-flash-preview` | chat | preview | text | 1M tokens | Preview |
| `models/gemini-3-pro-image-preview` | chat | preview | text, image | 131K tokens | Image capable |
| `models/gemini-2.5-flash` | chat | active | text | 1M tokens | |
| `models/gemini-2.5-pro` | chat | active | text | 1M tokens | |
| `models/gemini-2.5-flash-lite` | chat | active | text | 1M tokens | Lightweight |
| `models/gemini-2.0-flash` | chat | active | text | 1M tokens | |
| `models/gemini-2.0-flash-lite` | chat | active | text | 1M tokens | Lightweight |

---

**Note:** Model availability and status may vary by region and API access tier. Preview models may have limited availability or different pricing.