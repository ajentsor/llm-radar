#!/usr/bin/env python3
"""
LLM Radar MCP Server

A Model Context Protocol server that provides real-time AI model intelligence.
Exposes tools for querying, comparing, and getting recommendations about LLM models.

Usage:
    # Run with stdio transport (for Claude Desktop)
    llm-radar-mcp

    # Run with HTTP transport (for remote hosting)
    llm-radar-mcp --http --port 8000
"""

import argparse
import asyncio
import json
import sys
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Resource,
    TextContent,
    Tool,
)

# Resolve data directory
if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent.parent.parent

DATA_DIR = BASE_DIR / "data"


def load_models_data() -> dict:
    """Load the models.json data file."""
    models_file = DATA_DIR / "models.json"
    if not models_file.exists():
        return {"error": "models.json not found", "providers": {}}

    with open(models_file) as f:
        return json.load(f)


def get_all_models(data: dict) -> list[dict]:
    """Flatten all models from all providers into a single list."""
    models = []
    for provider_data in data.get("providers", {}).values():
        models.extend(provider_data.get("models", []))
    return models


def filter_models(
    models: list[dict],
    provider: str | None = None,
    capability: str | None = None,
    max_input_price: float | None = None,
    min_context: int | None = None,
) -> list[dict]:
    """Filter models by various criteria."""
    result = models

    if provider:
        result = [m for m in result if m.get("provider", "").lower() == provider.lower()]

    if capability:
        cap_lower = capability.lower()
        result = [
            m for m in result
            if any(cap_lower in c.lower() for c in m.get("capabilities", []))
        ]

    if max_input_price is not None:
        result = [
            m for m in result
            if m.get("pricing") and m["pricing"].get("input", float("inf")) <= max_input_price
        ]

    if min_context is not None:
        result = [
            m for m in result
            if m.get("context_window") and m["context_window"] >= min_context
        ]

    return result


def format_model_summary(model: dict) -> str:
    """Format a model into a readable summary."""
    pricing = model.get("pricing")
    price_str = (
        f"${pricing['input']:.2f}/${pricing['output']:.2f} per 1M tokens"
        if pricing else "Pricing unknown"
    )

    context = model.get("context_window")
    context_str = f"{context:,} tokens" if context else "Unknown"

    caps = ", ".join(model.get("capabilities", [])) or "None listed"

    return f"""**{model.get('name', model.get('id', 'Unknown'))}** ({model.get('provider', 'unknown')})
- ID: `{model.get('id', 'unknown')}`
- {model.get('description', 'No description')}
- Context: {context_str}
- Pricing: {price_str}
- Capabilities: {caps}
- Recommended for: {model.get('recommended_for', 'General use')}
- Status: {model.get('status', 'unknown')}"""


def format_comparison_table(models: list[dict]) -> str:
    """Format multiple models as a comparison table."""
    if not models:
        return "No models to compare."

    lines = ["| Model | Provider | Input $/1M | Output $/1M | Context | Capabilities |",
             "|-------|----------|------------|-------------|---------|--------------|"]

    for m in models:
        pricing = m.get("pricing", {})
        input_price = f"${pricing.get('input', '?')}" if pricing else "?"
        output_price = f"${pricing.get('output', '?')}" if pricing else "?"
        context = f"{m.get('context_window', '?'):,}" if m.get('context_window') else "?"
        caps = ", ".join(m.get("capabilities", [])[:3])
        if len(m.get("capabilities", [])) > 3:
            caps += "..."

        lines.append(
            f"| {m.get('name', m.get('id', '?'))} | {m.get('provider', '?')} | "
            f"{input_price} | {output_price} | {context} | {caps} |"
        )

    return "\n".join(lines)


def create_server() -> Server:
    """Create and configure the MCP server."""
    server = Server("llm-radar")

    @server.list_resources()
    async def list_resources() -> list[Resource]:
        """List available resources."""
        return [
            Resource(
                uri="llm-radar://models/all",
                name="All Models",
                description="Complete JSON data of all tracked AI models",
                mimeType="application/json",
            ),
            Resource(
                uri="llm-radar://models/openai",
                name="OpenAI Models",
                description="All OpenAI models (GPT-4, GPT-5, o1, o3, etc.)",
                mimeType="application/json",
            ),
            Resource(
                uri="llm-radar://models/anthropic",
                name="Anthropic Models",
                description="All Anthropic Claude models",
                mimeType="application/json",
            ),
            Resource(
                uri="llm-radar://models/google",
                name="Google Models",
                description="All Google Gemini models",
                mimeType="application/json",
            ),
            Resource(
                uri="llm-radar://highlights",
                name="Model Highlights",
                description="Curated recommendations: cheapest, most powerful, best for code, etc.",
                mimeType="application/json",
            ),
        ]

    @server.read_resource()
    async def read_resource(uri: str) -> str:
        """Read a specific resource."""
        data = load_models_data()

        if uri == "llm-radar://models/all":
            return json.dumps(data, indent=2)

        if uri == "llm-radar://highlights":
            return json.dumps(data.get("highlights", {}), indent=2)

        # Handle provider-specific resources
        provider_map = {
            "llm-radar://models/openai": "openai",
            "llm-radar://models/anthropic": "anthropic",
            "llm-radar://models/google": "google",
        }

        if uri in provider_map:
            provider = provider_map[uri]
            provider_data = data.get("providers", {}).get(provider, {})
            return json.dumps(provider_data, indent=2)

        return json.dumps({"error": f"Unknown resource: {uri}"})

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        """List available tools."""
        return [
            Tool(
                name="query_models",
                description="Search and filter AI models by provider, capability, price, or context window. Returns matching models with details.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "provider": {
                            "type": "string",
                            "description": "Filter by provider: 'openai', 'anthropic', or 'google'",
                            "enum": ["openai", "anthropic", "google"],
                        },
                        "capability": {
                            "type": "string",
                            "description": "Filter by capability: 'vision', 'reasoning', 'code', 'function_calling', etc.",
                        },
                        "max_input_price": {
                            "type": "number",
                            "description": "Maximum input price per 1M tokens in USD",
                        },
                        "min_context": {
                            "type": "integer",
                            "description": "Minimum context window size in tokens",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of results to return (default: 10)",
                            "default": 10,
                        },
                    },
                },
            ),
            Tool(
                name="compare_models",
                description="Compare specific models side-by-side. Provide model IDs to get a detailed comparison table.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "model_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of model IDs to compare (e.g., ['gpt-4o', 'claude-3-5-sonnet', 'gemini-1.5-pro'])",
                        },
                    },
                    "required": ["model_ids"],
                },
            ),
            Tool(
                name="get_model",
                description="Get detailed information about a specific model by ID.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "model_id": {
                            "type": "string",
                            "description": "The model ID (e.g., 'gpt-4o', 'claude-3-5-sonnet', 'gemini-1.5-pro')",
                        },
                    },
                    "required": ["model_id"],
                },
            ),
            Tool(
                name="get_recommendations",
                description="Get model recommendations for specific use cases like 'cheapest', 'most_powerful', 'best_for_code', 'largest_context'.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "use_case": {
                            "type": "string",
                            "description": "The use case to get recommendations for",
                            "enum": ["cheapest", "most_powerful", "best_for_code", "largest_context", "all"],
                        },
                    },
                    "required": ["use_case"],
                },
            ),
            Tool(
                name="get_pricing",
                description="Get pricing information for models, optionally filtered by provider or sorted by cost.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "provider": {
                            "type": "string",
                            "description": "Filter by provider",
                            "enum": ["openai", "anthropic", "google"],
                        },
                        "sort_by": {
                            "type": "string",
                            "description": "Sort by 'input' or 'output' price",
                            "enum": ["input", "output"],
                            "default": "input",
                        },
                        "ascending": {
                            "type": "boolean",
                            "description": "Sort in ascending order (cheapest first)",
                            "default": True,
                        },
                    },
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
        """Handle tool calls."""
        data = load_models_data()
        all_models = get_all_models(data)

        if name == "query_models":
            filtered = filter_models(
                all_models,
                provider=arguments.get("provider"),
                capability=arguments.get("capability"),
                max_input_price=arguments.get("max_input_price"),
                min_context=arguments.get("min_context"),
            )

            limit = arguments.get("limit", 10)
            filtered = filtered[:limit]

            if not filtered:
                return [TextContent(type="text", text="No models found matching your criteria.")]

            result = f"Found {len(filtered)} model(s):\n\n"
            result += format_comparison_table(filtered)
            result += "\n\n---\n\n"
            for m in filtered[:5]:  # Detailed info for first 5
                result += format_model_summary(m) + "\n\n"

            if len(filtered) > 5:
                result += f"_...and {len(filtered) - 5} more. Use get_model for details on specific models._"

            return [TextContent(type="text", text=result)]

        elif name == "compare_models":
            model_ids = arguments.get("model_ids", [])
            models_to_compare = []
            not_found = []

            for mid in model_ids:
                found = next(
                    (m for m in all_models if m.get("id", "").lower() == mid.lower()),
                    None
                )
                if found:
                    models_to_compare.append(found)
                else:
                    not_found.append(mid)

            result = ""
            if not_found:
                result += f"**Note:** Could not find: {', '.join(not_found)}\n\n"

            if models_to_compare:
                result += "## Model Comparison\n\n"
                result += format_comparison_table(models_to_compare)
                result += "\n\n### Details\n\n"
                for m in models_to_compare:
                    result += format_model_summary(m) + "\n\n---\n\n"
            else:
                result += "No valid models found to compare."

            return [TextContent(type="text", text=result)]

        elif name == "get_model":
            model_id = arguments.get("model_id", "")
            model = next(
                (m for m in all_models if m.get("id", "").lower() == model_id.lower()),
                None
            )

            if model:
                return [TextContent(type="text", text=format_model_summary(model))]
            else:
                # Try partial match
                partial_matches = [
                    m for m in all_models
                    if model_id.lower() in m.get("id", "").lower()
                ]
                if partial_matches:
                    result = f"Model '{model_id}' not found exactly. Did you mean:\n\n"
                    for m in partial_matches[:5]:
                        result += f"- `{m.get('id')}` ({m.get('provider')})\n"
                    return [TextContent(type="text", text=result)]

                return [TextContent(type="text", text=f"Model '{model_id}' not found.")]

        elif name == "get_recommendations":
            use_case = arguments.get("use_case", "all")
            highlights = data.get("highlights", {})

            if use_case == "all":
                result = "## Model Recommendations\n\n"
                for key, value in highlights.items():
                    result += f"**{key.replace('_', ' ').title()}:** {value}\n\n"
                return [TextContent(type="text", text=result)]

            key_map = {
                "cheapest": "cheapest_capable",
                "most_powerful": "most_powerful",
                "best_for_code": "best_for_code",
                "largest_context": "largest_context",
            }

            key = key_map.get(use_case)
            if key and key in highlights:
                return [TextContent(
                    type="text",
                    text=f"**{use_case.replace('_', ' ').title()}:** {highlights[key]}"
                )]

            return [TextContent(type="text", text=f"No recommendation found for '{use_case}'.")]

        elif name == "get_pricing":
            provider = arguments.get("provider")
            sort_by = arguments.get("sort_by", "input")
            ascending = arguments.get("ascending", True)

            models = filter_models(all_models, provider=provider)
            models_with_pricing = [m for m in models if m.get("pricing")]

            models_with_pricing.sort(
                key=lambda m: m["pricing"].get(sort_by, float("inf")),
                reverse=not ascending,
            )

            result = "## Pricing Comparison\n\n"
            result += f"Sorted by **{sort_by}** price ({'ascending' if ascending else 'descending'})\n\n"
            result += "| Model | Provider | Input $/1M | Output $/1M |\n"
            result += "|-------|----------|------------|-------------|\n"

            for m in models_with_pricing:
                p = m["pricing"]
                result += f"| {m.get('name', m.get('id'))} | {m.get('provider')} | ${p.get('input', '?')} | ${p.get('output', '?')} |\n"

            return [TextContent(type="text", text=result)]

        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    return server


async def run_stdio():
    """Run the server with stdio transport."""
    server = create_server()
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


async def run_http(host: str, port: int):
    """Run the server with HTTP/SSE transport."""
    from mcp.server.sse import SseServerTransport
    from starlette.applications import Starlette
    from starlette.routing import Route
    from starlette.responses import JSONResponse
    import uvicorn

    server = create_server()
    sse = SseServerTransport("/messages")

    async def handle_sse(request):
        async with sse.connect_sse(
            request.scope, request.receive, request._send
        ) as streams:
            await server.run(
                streams[0], streams[1], server.create_initialization_options()
            )

    async def handle_messages(request):
        await sse.handle_post_message(request.scope, request.receive, request._send)

    async def health(request):
        return JSONResponse({"status": "ok", "server": "llm-radar-mcp"})

    app = Starlette(
        routes=[
            Route("/health", health),
            Route("/sse", handle_sse),
            Route("/messages", handle_messages, methods=["POST"]),
        ]
    )

    config = uvicorn.Config(app, host=host, port=port)
    server_instance = uvicorn.Server(config)
    await server_instance.serve()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="LLM Radar MCP Server - Real-time AI Model Intelligence"
    )
    parser.add_argument(
        "--http",
        action="store_true",
        help="Run with HTTP/SSE transport instead of stdio",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Host to bind to (default: 0.0.0.0)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to listen on (default: 8000)",
    )

    args = parser.parse_args()

    if args.http:
        print(f"Starting LLM Radar MCP server on http://{args.host}:{args.port}")
        asyncio.run(run_http(args.host, args.port))
    else:
        asyncio.run(run_stdio())


if __name__ == "__main__":
    main()
