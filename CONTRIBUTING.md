# Contributing to LLM Radar

Thank you for your interest in contributing to LLM Radar! This document provides guidelines and instructions for contributing.

## Getting Started

### Prerequisites

- Python 3.10+
- Git
- API keys for testing (OpenAI, Anthropic, Google - optional)

### Local Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/ajentsor/llm-radar.git
   cd llm-radar
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in development mode**
   ```bash
   pip install -e ".[dev]"
   ```

4. **Set up environment variables** (optional, for data fetching)
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Running the MCP Server Locally

```bash
# stdio mode (for Claude Desktop)
llm-radar-mcp

# HTTP mode (for remote/testing)
llm-radar-mcp --http --port 8000
```

### Running Tests

```bash
pytest
```

## How to Contribute

### Reporting Bugs

- Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md)
- Include reproduction steps
- Include your environment details
- Attach relevant logs

### Suggesting Features

- Use the [feature request template](.github/ISSUE_TEMPLATE/feature_request.md)
- Explain the use case clearly
- Consider how it fits with existing functionality

### Submitting Code

1. **Fork the repository**

2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add tests for new functionality
   - Update documentation if needed

4. **Test your changes**
   ```bash
   pytest
   llm-radar-mcp --http &  # Start server
   # Test manually or with curl
   ```

5. **Commit your changes**
   ```bash
   git commit -m "feat: add your feature description"
   ```

   Follow [Conventional Commits](https://www.conventionalcommits.org/):
   - `feat:` for new features
   - `fix:` for bug fixes
   - `docs:` for documentation
   - `refactor:` for refactoring
   - `test:` for tests

6. **Push and create a Pull Request**
   ```bash
   git push origin feature/your-feature-name
   ```

## Code Style

- Use Python type hints
- Follow PEP 8 guidelines
- Use descriptive variable and function names
- Keep functions focused and small
- Add docstrings to public functions

## Project Structure

```
llm-radar/
├── src/llm_radar/          # Main package
│   ├── __init__.py
│   ├── mcp_server.py       # MCP server implementation
│   ├── fetch_models.py     # Data fetching from APIs
│   └── aggregate_with_claude.py  # Claude-powered enrichment
├── data/                   # Generated data
│   ├── models.json         # Structured model data
│   ├── MODELS.md          # Human-readable reference
│   └── raw/               # Raw API responses
├── docs/                   # Landing page (Cloudflare)
├── scripts/               # Utility scripts
└── tests/                 # Test files
```

## Areas for Contribution

### High Priority
- Additional provider support (Cohere, Mistral, etc.)
- More MCP tools (cost calculator, model recommender)
- Better error handling and edge cases
- Performance optimizations

### Documentation
- More examples in README
- API documentation
- Tutorials and guides

### Testing
- Unit tests for MCP tools
- Integration tests
- End-to-end tests with Claude Desktop

## Questions?

- Open an issue for questions
- Check existing issues first
- Be respectful and constructive

Thank you for contributing!
