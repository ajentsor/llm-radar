"""
Tests for the LLM Radar MCP Server.
"""

import json
import pytest
from pathlib import Path

# Add src to path
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from llm_radar.mcp_server import (
    create_server,
    load_models_data,
    get_all_models,
    filter_models,
    format_model_summary,
    format_comparison_table,
)


class TestDataLoading:
    """Test data loading functions."""

    def test_load_models_data(self):
        """Test that models.json loads correctly."""
        data = load_models_data()
        assert "providers" in data or "error" in data

        if "providers" in data:
            assert len(data["providers"]) > 0
            # Check we have at least one provider
            providers = list(data["providers"].keys())
            assert any(p in providers for p in ["openai", "anthropic", "google"])

    def test_get_all_models(self):
        """Test flattening all models."""
        data = load_models_data()
        if "error" not in data:
            models = get_all_models(data)
            assert isinstance(models, list)
            assert len(models) > 0
            # Each model should have an id
            for model in models:
                assert "id" in model or "name" in model


class TestFiltering:
    """Test model filtering functions."""

    @pytest.fixture
    def sample_models(self):
        """Sample models for testing."""
        return [
            {
                "id": "gpt-4o",
                "name": "GPT-4o",
                "provider": "openai",
                "capabilities": ["vision", "function_calling"],
                "pricing": {"input": 2.50, "output": 10.00},
                "context_window": 128000,
            },
            {
                "id": "claude-3-5-sonnet",
                "name": "Claude 3.5 Sonnet",
                "provider": "anthropic",
                "capabilities": ["vision", "code"],
                "pricing": {"input": 3.00, "output": 15.00},
                "context_window": 200000,
            },
            {
                "id": "gemini-1.5-pro",
                "name": "Gemini 1.5 Pro",
                "provider": "google",
                "capabilities": ["vision", "reasoning"],
                "pricing": {"input": 1.25, "output": 5.00},
                "context_window": 1000000,
            },
        ]

    def test_filter_by_provider(self, sample_models):
        """Test filtering by provider."""
        result = filter_models(sample_models, provider="openai")
        assert len(result) == 1
        assert result[0]["id"] == "gpt-4o"

    def test_filter_by_capability(self, sample_models):
        """Test filtering by capability."""
        result = filter_models(sample_models, capability="vision")
        assert len(result) == 3  # All have vision

        result = filter_models(sample_models, capability="code")
        assert len(result) == 1
        assert result[0]["id"] == "claude-3-5-sonnet"

    def test_filter_by_max_price(self, sample_models):
        """Test filtering by max input price."""
        result = filter_models(sample_models, max_input_price=2.00)
        assert len(result) == 1
        assert result[0]["id"] == "gemini-1.5-pro"

    def test_filter_by_min_context(self, sample_models):
        """Test filtering by minimum context window."""
        result = filter_models(sample_models, min_context=500000)
        assert len(result) == 1
        assert result[0]["id"] == "gemini-1.5-pro"

    def test_combined_filters(self, sample_models):
        """Test multiple filters together."""
        result = filter_models(
            sample_models,
            capability="vision",
            max_input_price=3.00,
        )
        assert len(result) == 3


class TestFormatting:
    """Test formatting functions."""

    def test_format_model_summary(self):
        """Test model summary formatting."""
        model = {
            "id": "gpt-4o",
            "name": "GPT-4o",
            "provider": "openai",
            "description": "Fast and capable multimodal model",
            "capabilities": ["vision", "function_calling"],
            "pricing": {"input": 2.50, "output": 10.00},
            "context_window": 128000,
            "recommended_for": "General tasks",
            "status": "active",
        }

        summary = format_model_summary(model)
        assert "GPT-4o" in summary
        assert "openai" in summary
        assert "$2.50" in summary
        assert "128,000 tokens" in summary

    def test_format_comparison_table(self):
        """Test comparison table formatting."""
        models = [
            {
                "id": "gpt-4o",
                "name": "GPT-4o",
                "provider": "openai",
                "capabilities": ["vision"],
                "pricing": {"input": 2.50, "output": 10.00},
                "context_window": 128000,
            },
        ]

        table = format_comparison_table(models)
        assert "| Model |" in table
        assert "GPT-4o" in table
        assert "openai" in table


class TestServerCreation:
    """Test MCP server creation."""

    def test_create_server(self):
        """Test that server creates successfully."""
        server = create_server()
        assert server is not None
        assert server.name == "llm-radar"


class TestMCPServerIntegration:
    """Test MCP server integration."""

    def test_server_has_name(self):
        """Test server has correct name."""
        server = create_server()
        assert server.name == "llm-radar"

    def test_server_creates_without_error(self):
        """Test server instantiation."""
        server = create_server()
        assert server is not None

    def test_data_file_exists_and_valid(self):
        """Test that the data file exists and is valid JSON."""
        data = load_models_data()

        # Should have providers or error
        if "error" not in data:
            assert "providers" in data
            assert "updated_at" in data or "summary" in data

            # Check structure
            for provider_name, provider_data in data["providers"].items():
                assert "models" in provider_data
                for model in provider_data["models"]:
                    # Each model should have required fields
                    assert "id" in model
                    assert "provider" in model


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
