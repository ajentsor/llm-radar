# AI Models Reference

**Last Updated:** 2025-12-28T13:34:03Z

**Summary:** 84 OpenAI models including GPT-5.2, GPT-5.1, O-series reasoning models, and GPT-4o variants; 8 Anthropic Claude models up to version 4.5; 32 Google Gemini models including 3.0 preview and 2.5/2.0 series.

---

## OpenAI

**API Documentation:** https://platform.openai.com/docs

| Model ID | Type | Status | Modalities |
|----------|------|--------|------------|
| `gpt-5.2-pro` | chat | active | text |
| `gpt-5.2` | chat | active | text |
| `gpt-5.1-codex-max` | chat | active | text |
| `gpt-5.1-codex` | chat | active | text |
| `gpt-5.1` | chat | active | text |
| `gpt-5-pro` | chat | active | text |
| `gpt-5-codex` | chat | active | text |
| `gpt-5-nano` | chat | active | text |
| `gpt-5-mini` | chat | active | text |
| `gpt-5` | chat | active | text |
| `o4-mini` | reasoning | active | text |
| `o3` | reasoning | active | text |
| `o3-mini` | reasoning | active | text |
| `o1-pro` | reasoning | active | text |
| `o1` | reasoning | active | text |
| `gpt-4.1-nano` | chat | active | text |
| `gpt-4.1-mini` | chat | active | text |
| `gpt-4.1` | chat | active | text |
| `gpt-4o-mini-search-preview` | chat | preview | text, image |
| `gpt-4o-search-preview` | chat | preview | text, image |
| `gpt-4o-mini-audio-preview` | audio | preview | text, image, audio |
| `gpt-4o-mini-realtime-preview` | audio | preview | text, image, audio |
| `gpt-4o-audio-preview` | audio | preview | text, image, audio |
| `gpt-4o-realtime-preview` | audio | preview | text, image, audio |
| `chatgpt-4o-latest` | chat | active | text, image |
| `gpt-4o` | chat | active | text, image |
| `gpt-4o-mini` | chat | active | text, image |
| `gpt-4-turbo` | chat | active | text |
| `gpt-4` | chat | active | text |
| `gpt-3.5-turbo` | chat | active | text |

---

## Anthropic

**API Documentation:** https://docs.anthropic.com

| Model ID | Type | Status | Modalities |
|----------|------|--------|------------|
| `claude-opus-4-5-20251101` | chat | active | text |
| `claude-haiku-4-5-20251001` | chat | active | text |
| `claude-sonnet-4-5-20250929` | chat | active | text |
| `claude-opus-4-1-20250805` | chat | active | text |
| `claude-opus-4-20250514` | chat | active | text |
| `claude-sonnet-4-20250514` | chat | active | text |
| `claude-3-5-haiku-20241022` | chat | active | text |
| `claude-3-haiku-20240307` | chat | active | text |

---

## Google

**API Documentation:** https://ai.google.dev/docs

| Model ID | Type | Status | Modalities |
|----------|------|--------|------------|
| `models/gemini-3-pro-preview` | chat | preview | text |
| `models/gemini-3-flash-preview` | chat | preview | text |
| `models/gemini-2.5-flash` | chat | active | text |
| `models/gemini-2.5-pro` | chat | active | text |
| `models/gemini-2.5-flash-lite` | chat | active | text |
| `models/gemini-2.0-flash-exp` | chat | preview | text |
| `models/gemini-2.0-flash` | chat | active | text |
| `models/gemini-2.0-flash-lite` | chat | active | text |

**Note:** All Google Gemini models have a context window of 1,048,576 tokens.