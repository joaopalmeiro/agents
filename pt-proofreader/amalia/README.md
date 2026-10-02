# amalia

[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

## Development

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) (if necessary):

```bash
curl -LsSf https://astral.sh/uv/0.11.6/install.sh | sh
```

```bash
uv python install
```

```bash
uv audit --verbose
```

```bash
uv run mypy
```

```bash
uv run ruff format
```

```bash
uv run ruff check --fix
```

```bash
MODAL_TOKEN_ID="op://Development/Modal/MODAL_TOKEN_ID" MODAL_TOKEN_SECRET="op://Development/Modal/MODAL_TOKEN_SECRET"  op run -- uv run modal deploy server.py
```

```bash
curl "$(op read op://Development/Modal/AMALIA_ENDPOINT)/v1/chat/completions" \
  --oauth2-bearer "$(op read op://Development/Modal/BEARER_TOKEN)" \
  --json '{"model": "amalia-llm/AMALIA-9B-0626-DPO", "messages": [{"role": "user", "content": "Olá"}]}'
```
