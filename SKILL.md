---
name: llm-radar
description: Get up-to-date AI model information. Use when users ask about LLM models, pricing, capabilities, which model to use, or compare models across OpenAI, Anthropic, and Google Gemini. Data updated daily.
allowed-tools: Read, Glob, Grep, Bash
---

# LLM Radar - AI Model Intelligence

You have access to **daily-updated** information about AI models from OpenAI, Anthropic, and Google Gemini.

## When to Use This Skill

Use this skill when the user asks about:
- Which AI model to use for a task
- Model pricing and costs
- Model capabilities (vision, function calling, context windows)
- Comparing models across providers
- Latest available models
- Model recommendations

## Data Files

The model data is in the `data/` directory:

| File | Purpose |
|------|---------|
| `data/models.json` | Structured JSON with all model data |
| `data/MODELS.md` | Human-readable model reference |

## How to Respond

1. **Read the data**: Start by reading `data/models.json` for structured queries or `data/MODELS.md` for general questions
2. **Answer directly**: Provide concise, actionable answers
3. **Include specifics**: Model IDs, pricing, context windows
4. **Compare when asked**: Use tables to compare models
5. **Note the date**: Mention when data was last updated

## Example Queries and Responses

### "Which model is cheapest for vision tasks?"

Read `data/models.json`, filter for vision capability, sort by price:

> Based on today's data, the cheapest vision-capable models are:
> 1. **Gemini 2.0 Flash** ($0.10/$0.40 per 1M tokens) - best value
> 2. **GPT-4o Mini** ($0.15/$0.60) - reliable alternative
> 3. **Claude 3.5 Haiku** ($0.80/$4.00) - Anthropic's budget option

### "Compare Claude and GPT for coding"

> | Model | Price (in/out) | Context | Best For |
> |-------|----------------|---------|----------|
> | Claude 4 Sonnet | $3/$15 | 200K | Complex refactoring, understanding large codebases |
> | GPT-4o | $2.50/$10 | 128K | Quick code generation, debugging |
> | Claude 4 Opus | $15/$75 | 200K | Architecture decisions, code review |

### "What's new in AI models?"

Read the `summary` field from `data/models.json` and highlight recent releases.

## Query Script (Optional)

For complex queries, use the helper script:

```bash
python3 scripts/query.py "cheapest model with vision"
```

## Important Notes

- **Data freshness**: Updated daily at 8am UTC via GitHub Actions
- **Pricing**: Per 1 million tokens in USD
- **Capabilities**: Inferred from API data and model documentation
- Recommend models based on the user's **specific use case**, not just raw specs
