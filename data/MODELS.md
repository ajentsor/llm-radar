# AI Models Reference

**Last Updated:** February 19, 2026  
**Summary:** 94 models accessible via API across OpenAI (84 models), Anthropic (10 models), and Google (26 models), including latest GPT-5.2, Claude 4.6, and Gemini 3 series.

## OpenAI Models

[API Documentation](https://platform.openai.com/docs) | [Website](https://openai.com)

| Model ID | Type | Status | Input Modalities | Output Modalities |
|----------|------|--------|------------------|-------------------|
| `gpt-5.2-codex` | Chat | Active | Text | Text |
| `chatgpt-image-latest` | Image | Active | Text | Image |
| `gpt-4o-mini-tts-2025-12-15` | Audio | Active | Text | Audio |
| `gpt-4o-mini-transcribe-2025-12-15` | Audio | Active | Audio | Text |
| `gpt-5.2-chat-latest` | Chat | Active | Text | Text |
| `gpt-5.2-pro` | Chat | Active | Text | Text |
| `gpt-5.2` | Chat | Active | Text | Text |
| `gpt-5.1-codex` | Chat | Active | Text | Text |
| `gpt-5.1` | Chat | Active | Text | Text |
| `gpt-5.1-chat-latest` | Chat | Active | Text | Text |
| `gpt-5-search-api` | Chat | Active | Text | Text |
| `gpt-5-pro` | Chat | Active | Text | Text |
| `gpt-5-codex` | Chat | Active | Text | Text |
| `gpt-5-nano` | Chat | Active | Text | Text |
| `gpt-5-mini` | Chat | Active | Text | Text |
| `gpt-5` | Chat | Active | Text | Text |
| `gpt-5-chat-latest` | Chat | Active | Text | Text |
| `o4-mini-deep-research` | Reasoning | Active | Text | Text |
| `gpt-4o-audio-preview-2025-06-03` | Audio | Preview | Text, Audio | Text, Audio |
| `gpt-4o-realtime-preview-2025-06-03` | Chat | Preview | Text, Audio | Text, Audio |
| `gpt-4.1` | Chat | Active | Text | Text |
| `o4-mini` | Reasoning | Active | Text | Text |
| `o3` | Reasoning | Active | Text | Text |
| `o1-pro` | Reasoning | Active | Text | Text |
| `gpt-4o-mini-search-preview` | Chat | Preview | Text | Text |
| `gpt-4o-search-preview` | Chat | Preview | Text | Text |
| `o3-mini` | Reasoning | Active | Text | Text |
| `gpt-4o-mini-audio-preview` | Audio | Preview | Text, Audio | Text, Audio |
| `gpt-4o-mini-realtime-preview` | Chat | Preview | Text, Audio | Text, Audio |
| `o1` | Reasoning | Active | Text | Text |
| `gpt-4o-realtime-preview` | Chat | Preview | Text, Audio | Text, Audio |
| `gpt-4o-audio-preview` | Audio | Preview | Text, Audio | Text, Audio |
| `gpt-4o-mini` | Chat | Active | Text, Image | Text |
| `gpt-4o` | Chat | Active | Text, Image | Text |
| `gpt-4-turbo` | Chat | Active | Text | Text |
| `gpt-4` | Chat | Active | Text | Text |
| `gpt-3.5-turbo` | Chat | Active | Text | Text |

## Anthropic Models

[API Documentation](https://docs.anthropic.com) | [Website](https://anthropic.com)

| Model ID | Type | Status | Input Modalities | Output Modalities |
|----------|------|--------|------------------|-------------------|
| `claude-sonnet-4-6` | Chat | Active | Text | Text |
| `claude-opus-4-6` | Chat | Active | Text | Text |
| `claude-opus-4-5-20251101` | Chat | Active | Text | Text |
| `claude-haiku-4-5-20251001` | Chat | Active | Text | Text |
| `claude-sonnet-4-5-20250929` | Chat | Active | Text | Text |
| `claude-opus-4-1-20250805` | Chat | Active | Text | Text |
| `claude-opus-4-20250514` | Chat | Active | Text | Text |
| `claude-sonnet-4-20250514` | Chat | Active | Text | Text |
| `claude-3-5-haiku-20241022` | Chat | Active | Text | Text |
| `claude-3-haiku-20240307` | Chat | Active | Text | Text |

## Google Models

[API Documentation](https://ai.google.dev/docs) | [Website](https://ai.google)

| Model ID | Type | Status | Input Modalities | Output Modalities |
|----------|------|--------|------------------|-------------------|
| `models/gemini-3-pro-preview` | Chat | Preview | Text | Text |
| `models/gemini-3-flash-preview` | Chat | Preview | Text | Text |
| `models/gemini-3-pro-image-preview` | Image | Preview | Text | Image |
| `models/gemini-2.5-flash` | Chat | Active | Text | Text |
| `models/gemini-2.5-pro` | Chat | Active | Text | Text |
| `models/gemini-2.5-flash-preview-tts` | Audio | Preview | Text | Audio |
| `models/gemini-2.5-pro-preview-tts` | Audio | Preview | Text | Audio |
| `models/gemini-2.5-flash-lite` | Chat | Active | Text | Text |
| `models/gemini-2.5-flash-image` | Image | Active | Text | Image |
| `models/gemini-2.5-computer-use-preview-10-2025` | Chat | Preview | Text | Text |
| `models/gemini-2.5-flash-native-audio-latest` | Audio | Active | Text, Audio | Text, Audio |
| `models/gemini-2.0-flash` | Chat | Active | Text | Text |
| `models/gemini-2.0-flash-exp-image-generation` | Image | Preview | Text | Image |
| `models/gemini-2.0-flash-lite` | Chat | Active | Text | Text |

## Notes

- **Multimodal Support**: Models with "Text, Image" or "Text, Audio" input support multiple input types
- **Status**: Active (production ready), Preview (experimental/beta)
- **Model Types**: Chat (text generation), Image (image generation), Audio (speech synthesis/recognition), Reasoning (advanced problem solving)