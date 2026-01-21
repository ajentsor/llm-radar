# AI Models API Reference

**Last Updated:** 2026-01-21 08:31:42 UTC

**Summary:** 85 OpenAI models (including GPT-5.2, GPT-5.1, GPT-5, O-series, and GPT-4o variants), 8 Anthropic Claude models (up to Claude Opus 4.5), and 31 Google Gemini models (up to Gemini 3 Pro Preview) are currently accessible via API.

## OpenAI Models

**Provider:** [OpenAI](https://openai.com) | **API Docs:** [platform.openai.com/docs](https://platform.openai.com/docs)

| Model ID | Type | Status | Input | Notes |
|----------|------|--------|-------|-------|
| `gpt-5.2-codex` | chat | active | text | Advanced coding-focused model |
| `gpt-5.2-chat-latest` | chat | active | text | Latest chat variant |
| `gpt-5.2-pro` | chat | active | text | Professional-grade variant |
| `gpt-5.2` | chat | active | text | Base GPT-5.2 model |
| `gpt-5.1-codex-max` | chat | active | text | Maximum-capability coding model |
| `gpt-5.1-codex` | chat | active | text | Coding-focused model |
| `gpt-5.1-chat-latest` | chat | active | text | Latest chat variant |
| `gpt-5.1` | chat | active | text | Base GPT-5.1 model |
| `gpt-5-search-api` | chat | active | text | Search-enhanced GPT-5 |
| `gpt-5-pro` | chat | active | text | Professional-grade variant |
| `gpt-5-codex` | chat | active | text | Coding-focused variant |
| `gpt-5-chat-latest` | chat | active | text | Latest chat variant |
| `gpt-5-nano` | chat | active | text | Compact variant |
| `gpt-5-mini` | chat | active | text | Smaller, efficient variant |
| `gpt-5` | chat | active | text | Base GPT-5 model |
| `gpt-4.1` | chat | active | text | Base GPT-4.1 model |
| `chatgpt-4o-latest` | chat | active | text, image | Latest ChatGPT 4o |
| `gpt-4o-mini` | chat | active | text, image | Smaller, efficient GPT-4o |
| `gpt-4o` | chat | active | text, image | Omni-modal GPT-4 variant |
| `gpt-4-turbo` | chat | active | text | Enhanced speed variant |
| `gpt-4` | chat | active | text | Base GPT-4 model |
| `gpt-3.5-turbo` | chat | active | text | Enhanced speed GPT-3.5 |

### O-Series (Reasoning Models)

| Model ID | Type | Status | Input | Notes |
|----------|------|--------|-------|-------|
| `o4-mini-deep-research` | reasoning | active | text | Deep research-focused |
| `o4-mini` | reasoning | active | text | Smaller O4 variant |
| `o3` | reasoning | active | text | Advanced reasoning model |
| `o3-mini` | reasoning | active | text | Smaller O3 variant |
| `o1-pro` | reasoning | active | text | Professional-grade O1 |
| `o1` | reasoning | active | text | Base O1 reasoning model |

### Audio Models

| Model ID | Type | Status | Input | Output | Notes |
|----------|------|--------|-------|--------|-------|
| `gpt-4o-mini-tts-2025-12-15` | audio | active | text | audio | Text-to-speech |
| `gpt-4o-mini-transcribe-2025-12-15` | audio | active | audio | text | Audio transcription |
| `gpt-4o-audio-preview-2025-06-03` | audio | preview | text, audio | text, audio | Audio-capable preview |
| `gpt-4o-realtime-preview-2025-06-03` | audio | preview | text, audio | text, audio | Real-time audio |
| `gpt-4o-mini-audio-preview` | audio | preview | text, audio | text, audio | Mini audio preview |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, audio | text, audio | Mini real-time audio |
| `gpt-4o-realtime-preview` | audio | preview | text, audio | text, audio | Real-time audio |
| `gpt-4o-audio-preview` | audio | preview | text, audio | text, audio | Audio-capable preview |

### Search & Specialized Models

| Model ID | Type | Status | Input | Notes |
|----------|------|--------|-------|-------|
| `gpt-4o-mini-search-preview` | chat | preview | text | Search-enhanced Mini |
| `gpt-4o-search-preview` | chat | preview | text | Search-enhanced GPT-4o |
| `chatgpt-image-latest` | image | active | text | Latest image capabilities |

## Anthropic Models

**Provider:** [Anthropic](https://anthropic.com) | **API Docs:** [docs.anthropic.com](https://docs.anthropic.com)

| Model ID | Type | Status | Input | Notes |
|----------|------|--------|-------|-------|
| `claude-opus-4-5-20251101` | chat | active | text | Latest Opus 4.5 |
| `claude-sonnet-4-5-20250929` | chat | active | text | Balanced 4.5 model |
| `claude-haiku-4-5-20251001` | chat | active | text | Fast, efficient 4.5 |
| `claude-opus-4-1-20250805` | chat | active | text | Powerful 4.1 model |
| `claude-opus-4-20250514` | chat | active | text | Powerful Claude 4 |
| `claude-sonnet-4-20250514` | chat | active | text | Balanced Claude 4 |
| `claude-3-5-haiku-20241022` | chat | active | text | Fast, efficient 3.5 |
| `claude-3-haiku-20240307` | chat | active | text | Fast, efficient Claude 3 |

## Google Models

**Provider:** [Google](https://ai.google.dev) | **API Docs:** [ai.google.dev/docs](https://ai.google.dev/docs)

| Model ID | Type | Status | Context | Notes |
|----------|------|--------|---------|-------|
| `models/gemini-3-pro-preview` | chat | preview | 1M | Gemini 3 Pro preview |
| `models/gemini-3-flash-preview` | chat | preview | 1M | Gemini 3 Flash preview |
| `models/gemini-2.5-pro` | chat | active | 1M | Professional 2.5 model |
| `models/gemini-2.5-flash` | chat | active | 1M | Fast, efficient 2.5 |
| `models/gemini-2.5-flash-lite` | chat | active | 1M | Lightweight 2.5 Flash |
| `models/gemini-2.0-flash-exp` | chat | preview | 1M | Experimental 2.0 Flash |
| `models/gemini-2.0-flash` | chat | active | 1M | Fast, efficient 2.0 |
| `models/gemini-2.0-flash-lite` | chat | active | 1M | Lightweight 2.0 Flash |

## Legend

- **Context:** 1M = 1,048,576 tokens
- **Status:** `active` (production ready), `preview` (experimental/limited access)
- **Input:** Supported input modalities (text, image, audio)
- **Type:** Model category (chat, reasoning, audio, image)