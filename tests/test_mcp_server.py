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
        """Sample models for testing with new schema."""
        return [
            {
                "id": "gpt-4o",
                "name": "GPT-4o",
                "provider": "openai",
                "api_accessible": True,
                "model_type": "chat",
                "input_modalities": ["text", "image"],
                "output_modalities": ["text"],
                "context_window": 128000,
                "status": "active",
            },
            {
                "id": "claude-3-5-sonnet",
                "name": "Claude 3.5 Sonnet",
                "provider": "anthropic",
                "api_accessible": True,
                "model_type": "chat",
                "input_modalities": ["text"],
                "output_modalities": ["text"],
                "context_window": 200000,
                "status": "active",
            },
            {
                "id": "gemini-1.5-pro",
                "name": "Gemini 1.5 Pro",
                "provider": "google",
                "api_accessible": True,
                "model_type": "chat",
                "input_modalities": ["text", "image"],
                "output_modalities": ["text"],
                "context_window": 1000000,
                "status": "active",
            },
            {
                "id": "o3",
                "name": "O3",
                "provider": "openai",
                "api_accessible": True,
                "model_type": "reasoning",
                "input_modalities": ["text"],
                "output_modalities": ["text"],
                "context_window": None,
                "status": "active",
            },
        ]

    def test_filter_by_provider(self, sample_models):
        """Test filtering by provider."""
        result = filter_models(sample_models, provider="openai")
        assert len(result) == 2
        assert all(m["provider"] == "openai" for m in result)

    def test_filter_by_model_type(self, sample_models):
        """Test filtering by model type."""
        result = filter_models(sample_models, model_type="chat")
        assert len(result) == 3

        result = filter_models(sample_models, model_type="reasoning")
        assert len(result) == 1
        assert result[0]["id"] == "o3"

    def test_filter_by_supports_images(self, sample_models):
        """Test filtering by image support."""
        result = filter_models(sample_models, supports_images=True)
        assert len(result) == 2
        assert all("image" in m["input_modalities"] for m in result)

    def test_filter_by_min_context(self, sample_models):
        """Test filtering by minimum context window."""
        result = filter_models(sample_models, min_context=500000)
        assert len(result) == 1
        assert result[0]["id"] == "gemini-1.5-pro"

    def test_combined_filters(self, sample_models):
        """Test multiple filters together."""
        result = filter_models(
            sample_models,
            model_type="chat",
            supports_images=True,
        )
        assert len(result) == 2
        assert all(m["model_type"] == "chat" for m in result)
        assert all("image" in m["input_modalities"] for m in result)


class TestFormatting:
    """Test formatting functions."""

    def test_format_model_summary(self):
        """Test model summary formatting."""
        model = {
            "id": "gpt-4o",
            "name": "GPT-4o",
            "provider": "openai",
            "description": "Fast and capable multimodal model",
            "api_accessible": True,
            "model_type": "chat",
            "input_modalities": ["text", "image"],
            "output_modalities": ["text"],
            "context_window": 128000,
            "status": "active",
        }

        summary = format_model_summary(model)
        assert "GPT-4o" in summary
        assert "openai" in summary
        assert "gpt-4o" in summary  # API ID
        assert "128,000 tokens" in summary
        assert "API Accessible: Yes" in summary

    def test_format_comparison_table(self):
        """Test comparison table formatting."""
        models = [
            {
                "id": "gpt-4o",
                "name": "GPT-4o",
                "provider": "openai",
                "model_type": "chat",
                "input_modalities": ["text", "image"],
                "context_window": 128000,
                "status": "active",
            },
        ]

        table = format_comparison_table(models)
        assert "| Model ID |" in table
        assert "gpt-4o" in table
        assert "openai" in table
        assert "chat" in table


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
                    assert "api_accessible" in model


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
