#!/usr/bin/env python3
"""
Simple query helper for the LLM Radar MCP server.
Usage: python query.py "cheapest model with vision"
"""

import json
import sys
from pathlib import Path

# Find the data directory relative to this script
SCRIPT_DIR = Path(__file__).parent
DATA_FILE = SCRIPT_DIR.parent / "data" / "models.json"


def load_models():
    """Load models from JSON file"""
    if not DATA_FILE.exists():
        print(f"Error: Data file not found at {DATA_FILE}")
        print("Run the fetch and aggregate scripts first.")
        sys.exit(1)

    with open(DATA_FILE) as f:
        return json.load(f)


def get_all_models(data):
    """Flatten all models from all providers"""
    models = []
    for provider_data in data.get("providers", {}).values():
        for model in provider_data.get("models", []):
            models.append(model)
    return models


def filter_by_capability(models, capability):
    """Filter models that have a specific capability"""
    return [m for m in models if capability in m.get("capabilities", [])]


def filter_by_provider(models, provider):
    """Filter models by provider name"""
    return [m for m in models if m.get("provider", "").lower() == provider.lower()]


def sort_by_price(models, ascending=True):
    """Sort models by input price (cheapest first by default)"""
    def get_price(m):
        pricing = m.get("pricing")
        if pricing and pricing.get("input"):
            return pricing["input"]
        return float("inf")  # Models without pricing go last

    return sorted(models, key=get_price, reverse=not ascending)


def format_table(models, limit=10):
    """Format models as a simple table"""
    lines = [
        "| Model | Provider | Price (in/out) | Capabilities |",
        "|-------|----------|----------------|--------------|"
    ]

    for m in models[:limit]:
        pricing = m.get("pricing")
        if pricing:
            price_str = f"${pricing.get('input', '?')}/{pricing.get('output', '?')}"
        else:
            price_str = "TBA"

        caps = ", ".join(m.get("capabilities", [])[:3])

        lines.append(f"| {m['name']} | {m['provider']} | {price_str} | {caps} |")

    return "\n".join(lines)


def process_query(query):
    """Process a natural language query about models"""
    query_lower = query.lower()
    data = load_models()
    models = get_all_models(data)

    # Parse query for filters
    results = models

    # Check for capability filters
    capabilities = ["vision", "reasoning", "code", "function_calling", "streaming", "thinking"]
    for cap in capabilities:
        if cap in query_lower:
            results = filter_by_capability(results, cap)

    # Check for provider filters
    providers = {
        "openai": ["openai", "gpt", "o1", "o3"],
        "anthropic": ["anthropic", "claude"],
        "google": ["google", "gemini"]
    }
    for provider, keywords in providers.items():
        if any(kw in query_lower for kw in keywords):
            results = filter_by_provider(results, provider)
            break

    # Check for sorting preferences
    if any(word in query_lower for word in ["cheap", "affordable", "budget", "lowest price"]):
        results = sort_by_price(results, ascending=True)
    elif any(word in query_lower for word in ["expensive", "premium", "best", "powerful"]):
        results = sort_by_price(results, ascending=False)

    # Output
    print(f"\n## Results for: {query}\n")
    print(format_table(results))
    print(f"\n*Data updated: {data.get('updated_at', 'unknown')}*")


def main():
    if len(sys.argv) < 2:
        print("Usage: python query.py <query>")
        print("\nExamples:")
        print('  python query.py "cheapest vision model"')
        print('  python query.py "compare claude models"')
        print('  python query.py "openai reasoning models"')
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    process_query(query)


if __name__ == "__main__":
    main()
