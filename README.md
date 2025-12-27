<div align="center">

# LLM Radar

### Real-time AI Model Intelligence for Developers

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org)
[![Updated Daily](https://img.shields.io/badge/data-updated%20daily-brightgreen.svg)](data/)
[![Claude Code Skill](https://img.shields.io/badge/claude%20code-skill-purple.svg)](SKILL.md)

**Stop guessing which AI model to use. Get the data.**

[Live Dashboard](https://ajentsor.github.io/llm-radar) &bull; [Model Reference](data/MODELS.md) &bull; [Install Skill](#install-as-claude-code-skill) &bull; [Contributing](#contributing)

</div>

---

## The Problem

Every time you ask an AI assistant about models, you get **outdated information**. Training data cutoffs mean AI assistants recommend old models, wrong pricing, or deprecated APIs.

## The Solution

**LLM Radar** fetches fresh data from OpenAI, Anthropic, and Google APIs **every day**, uses Claude to intelligently enrich it, and makes it available as:

- A **Claude Code skill** you can query naturally
- A **JSON API** for your applications
- A **beautiful dashboard** for quick reference

---

## Quick Start

### Install as Claude Code Skill

Clone into your Claude skills directory:

```bash
git clone https://github.com/ajentsor/llm-radar.git ~/.claude/skills/llm-radar
```

Then just ask Claude naturally:

```
> Which model is cheapest for vision tasks?

Based on the latest LLM Radar data (updated today):

1. **Gemini 2.0 Flash** - $0.10/$0.40 per 1M tokens
2. **GPT-4o Mini** - $0.15/$0.60 per 1M tokens
3. **Claude 3.5 Haiku** - $0.80/$4.00 per 1M tokens
```

### Use the Data Directly

```bash
# Get the JSON
curl -O https://raw.githubusercontent.com/ajentsor/llm-radar/main/data/models.json

# Use in Python
import json
with open('models.json') as f:
    data = json.load(f)
    for provider in data['providers'].values():
        for model in provider['models']:
            print(f"{model['name']}: ${model['pricing']['input']}/1M in")
```

### Run Locally

```bash
git clone https://github.com/ajentsor/llm-radar.git
cd llm-radar
pip install -r requirements.txt

# Fetch fresh data
python src/fetch_models.py

# Enrich with Claude
python src/aggregate_with_claude.py
```

---

## How It Works

```
┌─────────────────────────────────────────────────────────────────┐
│                    Daily GitHub Action (8am UTC)                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐                    │
│  │  OpenAI  │   │Anthropic │   │  Google  │   ← Fetch APIs     │
│  │   API    │   │   API    │   │   API    │                    │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘                    │
│       │              │              │                           │
│       └──────────────┼──────────────┘                           │
│                      ▼                                          │
│              ┌──────────────┐                                   │
│              │    Claude    │   ← Enrich & Format               │
│              │   (Sonnet)   │                                   │
│              └──────┬───────┘                                   │
│                     │                                           │
│       ┌─────────────┼─────────────┐                            │
│       ▼             ▼             ▼                            │
│  ┌─────────┐  ┌──────────┐  ┌───────────┐                      │
│  │models.  │  │ MODELS.  │  │  GitHub   │   ← Commit & Deploy  │
│  │  json   │  │   md     │  │  Pages    │                      │
│  └─────────┘  └──────────┘  └───────────┘                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

1. **Fetch**: GitHub Action calls OpenAI, Anthropic, and Google APIs
2. **Enrich**: Claude Sonnet processes raw data, adds descriptions, and generates human-readable docs
3. **Deploy**: Updated data is committed and GitHub Pages refreshes

---

## Data Available

Each model includes:

| Field | Description |
|-------|-------------|
| `id` | API model identifier |
| `name` | Human-friendly name |
| `provider` | openai, anthropic, or google |
| `description` | What the model is best for |
| `context_window` | Max input tokens |
| `pricing` | Input/output cost per 1M tokens |
| `capabilities` | vision, function_calling, streaming, etc. |
| `status` | active, preview, or deprecated |
| `released` | Release date |
| `recommended_for` | Use case suggestions |

---

## Project Structure

```
llm-radar/                   # Clone directly to ~/.claude/skills/llm-radar
├── SKILL.md                 # Claude Code skill definition
├── scripts/
│   └── query.py             # Query helper script
├── data/
│   ├── models.json          # Structured model data
│   ├── MODELS.md            # Human-readable reference
│   └── raw/                 # Raw API responses
├── src/
│   ├── fetch_models.py      # API fetchers
│   └── aggregate_with_claude.py  # Claude enrichment
├── docs/                    # GitHub Pages site
├── .github/workflows/
│   └── update-models.yml    # Daily cron using Claude
└── README.md
```

---

## Configuration

To run the updater yourself, you need API keys:

```bash
# .env file
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
GOOGLE_API_KEY=AI...
```

For GitHub Actions, add these as repository secrets.

---

## Contributing

Contributions welcome! Here's how to help:

- **Add a provider**: Create a new fetcher in `src/fetchers/`
- **Improve enrichment**: Update the Claude prompt in `aggregate_with_claude.py`
- **Fix pricing**: Update `PRICING_DATA` with latest prices
- **Enhance the skill**: Improve `SKILL.md` for better Claude responses

---

## Why This Exists

AI assistants have training data cutoffs. When you ask about models:
- You get **old model recommendations** (GPT-4 instead of GPT-4o)
- **Wrong pricing** (models get cheaper over time)
- **Missing new models** (o3, Claude 4.5, Gemini 2.5)

LLM Radar solves this by maintaining a **living dataset** that updates daily and integrates directly with Claude Code.

---

## License

MIT License - see [LICENSE](LICENSE)

---

<div align="center">

**Built for developers who want accurate AI model info**

[Star this repo](https://github.com/ajentsor/llm-radar) &bull; [Report Issue](https://github.com/ajentsor/llm-radar/issues) &bull; [View Dashboard](https://ajentsor.github.io/llm-radar)

</div>
