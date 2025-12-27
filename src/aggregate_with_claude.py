#!/usr/bin/env python3
"""
Use Claude (Anthropic API) to intelligently aggregate and enrich model data.
This script reads raw API responses and uses Claude to:
1. Normalize and structure the data
2. Add helpful descriptions and context
3. Generate a human-readable MODELS.md
4. Track what's new/changed since last update
"""

import json
import os
from datetime import datetime, timezone
from pathlib import Path

import anthropic
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"

# Known pricing data (not available via API, so we maintain it here)
# Prices are per 1M tokens in USD
PRICING_DATA = {
    # OpenAI - GPT-5.x series
    "gpt-5.2": {"input": 1.75, "output": 14.00},
    "gpt-5.2-pro": {"input": 3.50, "output": 28.00},
    "gpt-5.1": {"input": 1.25, "output": 10.00},
    "gpt-5": {"input": 1.00, "output": 8.00},
    # OpenAI - GPT-4.x series
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "gpt-4-turbo": {"input": 10.00, "output": 30.00},
    "gpt-4": {"input": 30.00, "output": 60.00},
    "gpt-3.5-turbo": {"input": 0.50, "output": 1.50},
    # OpenAI - o-series reasoning
    "o4-mini": {"input": 1.50, "output": 6.00},
    "o3": {"input": 20.00, "output": 80.00},
    "o3-mini": {"input": 1.10, "output": 4.40},
    "o1": {"input": 15.00, "output": 60.00},
    "o1-mini": {"input": 3.00, "output": 12.00},
    "o1-pro": {"input": 150.00, "output": 600.00},
    # Anthropic
    "claude-opus-4-5": {"input": 15.00, "output": 75.00},
    "claude-sonnet-4-5": {"input": 3.00, "output": 15.00},
    "claude-haiku-4-5": {"input": 1.00, "output": 5.00},
    "claude-opus-4": {"input": 15.00, "output": 75.00},
    "claude-sonnet-4": {"input": 3.00, "output": 15.00},
    "claude-3-5-sonnet": {"input": 3.00, "output": 15.00},
    "claude-3-5-haiku": {"input": 0.80, "output": 4.00},
    "claude-3-opus": {"input": 15.00, "output": 75.00},
    "claude-3-sonnet": {"input": 3.00, "output": 15.00},
    "claude-3-haiku": {"input": 0.25, "output": 1.25},
    # Google - Gemini 3.x series
    "gemini-3-flash": {"input": 0.50, "output": 3.00},
    "gemini-3-pro": {"input": 2.00, "output": 10.00},
    # Google - Gemini 2.x series
    "gemini-2.5-pro": {"input": 1.25, "output": 10.00},
    "gemini-2.5-flash": {"input": 0.15, "output": 0.60},
    "gemini-2.0-flash": {"input": 0.10, "output": 0.40},
    "gemini-2.0-flash-thinking": {"input": 0.70, "output": 3.50},
    "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
    "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
}


def load_raw_data() -> dict:
    """Load the latest raw API data"""
    raw_file = RAW_DIR / "latest.json"
    if not raw_file.exists():
        raise FileNotFoundError(f"No raw data found at {raw_file}. Run fetch_models.py first.")

    with open(raw_file) as f:
        return json.load(f)


def load_previous_data() -> dict | None:
    """Load previous aggregated data for comparison"""
    models_file = DATA_DIR / "models.json"
    if models_file.exists():
        with open(models_file) as f:
            return json.load(f)
    return None


def aggregate_with_claude(raw_data: dict, previous_data: dict | None = None) -> tuple[dict, str]:
    """
    Use Claude to process raw API data into structured, enriched format.
    Returns (models_json, models_markdown)
    """
    client = anthropic.Anthropic()

    # Prepare context about previous data for change detection
    previous_context = ""
    if previous_data:
        prev_models = []
        for provider_data in previous_data.get("providers", {}).values():
            for m in provider_data.get("models", []):
                prev_models.append(f"{m.get('provider', 'unknown')}/{m.get('id', 'unknown')}")
        previous_context = f"\n\nPreviously tracked models: {', '.join(prev_models[:50])}"

    # Sort Google models to prioritize newest (Gemini 3 > 2.5 > 2.0 > 1.5)
    google_data = raw_data.get('google', {})
    if 'models' in google_data:
        def model_priority(m):
            name = m.get('name', '').lower()
            if 'gemini-3' in name: return 0
            if 'gemini-2.5' in name: return 1
            if 'gemini-2.0' in name or 'gemini-2-' in name: return 2
            if 'gemini-1.5' in name: return 3
            return 4
        google_data['models'] = sorted(google_data['models'], key=model_priority)

    prompt = f"""You are an AI model data curator. Analyze the raw API responses from OpenAI, Anthropic, and Google, and create a structured JSON output with enriched information about each model.

## Raw API Data

### OpenAI Models
```json
{json.dumps(raw_data.get('openai', {}), indent=2)[:12000]}
```

### Anthropic Models
```json
{json.dumps(raw_data.get('anthropic', {}), indent=2)[:8000]}
```

### Google Gemini Models
```json
{json.dumps(google_data, indent=2)[:12000]}
```

## Known Pricing (per 1M tokens USD)
```json
{json.dumps(PRICING_DATA, indent=2)}
```
{previous_context}

## Your Task

Create a JSON object with this structure:
```json
{{
  "updated_at": "<current ISO timestamp>",
  "summary": "<1-2 sentence summary of what's notable - new models, key updates>",
  "providers": {{
    "openai": {{
      "name": "OpenAI",
      "website": "https://openai.com",
      "models": [
        {{
          "id": "<model id for API calls>",
          "name": "<human-friendly name>",
          "provider": "openai",
          "description": "<1 sentence: what this model is best for>",
          "context_window": <number or null>,
          "pricing": {{"input": <$/1M>, "output": <$/1M>}} or null,
          "capabilities": ["<list of: vision, function_calling, streaming, reasoning, code, etc>"],
          "status": "<active|preview|deprecated>",
          "released": "<YYYY-MM-DD or null>",
          "recommended_for": "<use case: e.g., 'General chat, code generation'>"
        }}
      ]
    }},
    "anthropic": {{ ... }},
    "google": {{ ... }}
  }},
  "highlights": {{
    "cheapest_capable": "<model id> - <brief why>",
    "most_powerful": "<model id> - <brief why>",
    "best_for_code": "<model id> - <brief why>",
    "largest_context": "<model id> - <context size>"
  }}
}}
```

## Guidelines
1. Include all significant models - both production AND preview for newest model families (e.g., Gemini 3, GPT-5.2). Skip deprecated, internal, or embedding-only models.
2. For each model, infer capabilities from the name and your knowledge
3. Use the pricing data provided, or null if unknown
4. For descriptions, be concise and practical - what would a developer want to know?
5. In the summary, mention if any models are NEW (not in previous list) or notable updates
6. IMPORTANT: Include Gemini 3 models even if marked as preview - they are the newest Google models
7. Current date: {datetime.now(timezone.utc).strftime("%Y-%m-%d")}

Output ONLY the JSON, no markdown code blocks or explanations."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}]
    )

    # Parse Claude's response
    json_text = response.content[0].text.strip()
    # Remove any markdown code blocks if present
    if json_text.startswith("```"):
        json_text = json_text.split("```")[1]
        if json_text.startswith("json"):
            json_text = json_text[4:]
    if json_text.endswith("```"):
        json_text = json_text[:-3]

    models_data = json.loads(json_text.strip())

    # Now generate the markdown version
    markdown = generate_markdown(models_data)

    return models_data, markdown


def generate_markdown(data: dict) -> str:
    """Generate a beautiful MODELS.md from the structured data"""
    client = anthropic.Anthropic()

    prompt = f"""Generate a beautiful, well-organized Markdown document for developers showing the latest AI models.

Data:
```json
{json.dumps(data, indent=2)}
```

Create a MODELS.md with:
1. A header with the update date and a brief summary
2. A "Highlights" section with the best models for different use cases
3. Organized sections for each provider (OpenAI, Anthropic, Google)
4. For each model: name, description, key specs (context, pricing), capabilities as badges
5. Use tables where appropriate for easy scanning
6. Keep it concise but informative - developers should be able to quickly find what they need

Make it beautiful with good formatting, emoji sparingly for visual interest, and clear hierarchy.

Output ONLY the markdown content, ready to save as MODELS.md."""

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4000,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text.strip()


def save_outputs(models_data: dict, markdown: str):
    """Save the processed data"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Save JSON
    with open(DATA_DIR / "models.json", "w") as f:
        json.dump(models_data, f, indent=2)
    print(f"Saved {DATA_DIR / 'models.json'}")

    # Save Markdown
    with open(DATA_DIR / "MODELS.md", "w") as f:
        f.write(markdown)
    print(f"Saved {DATA_DIR / 'MODELS.md'}")


def main():
    print("Loading raw API data...")
    raw_data = load_raw_data()

    print("Loading previous data for comparison...")
    previous_data = load_previous_data()

    print("Asking Claude to aggregate and enrich the data...")
    models_data, markdown = aggregate_with_claude(raw_data, previous_data)

    print("Saving outputs...")
    save_outputs(models_data, markdown)

    print(f"\nDone! Summary: {models_data.get('summary', 'No summary')}")


if __name__ == "__main__":
    main()
