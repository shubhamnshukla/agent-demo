# Luumen Support Agent

AI-powered customer support agent for [Luumen](https://www.luumen.ai), built on the [`definable`](https://pypi.org/project/definable/) framework.

Answers user questions from a markdown knowledge base, guarded by input/output/tool guardrails, hardened with a security policy, traced to JSONL, with persistent SQLite memory.

## Stack

| Concern | Implementation |
|---------|----------------|
| Model | `gpt-5.4-nano` (OpenAI) |
| Knowledge base | `app/kb/*.md` — auto-indexed via `Knowledge.from_path` (InMemoryVectorDB + OpenAIEmbedder) |
| Memory | `SQLiteStore("./memory.db")` |
| Tracing | `JSONLExporter("./traces")` |
| Guardrails | `max_tokens`, `pii_filter`, `tool_blocklist`, custom `no_profanity` |
| Security | `ToolPolicy` allowlist, `RateLimitConfig`, `ContentDefenseConfig`, `SSRFGuardConfig`, `EnvSanitizeConfig` |
| Skills | `Calculator`, `DateTime`, `customer_support_reply` |
| Observability | `observability=True`, `thinking=True`, `debug=True` |
| Server | `agent.serve(enable_server=True)` — FastAPI |

## Project Layout

```
agents/
├── main.py                    entrypoint
├── pyproject.toml
├── README.md
└── app/
    ├── __init__.py
    ├── agent.py               Agent instance
    ├── guardrails/
    │   ├── config.py          Guardrails(...) bundle
    │   └── custom.py          no_profanity factory
    ├── security/
    │   └── config.py          SecurityConfig(...)
    ├── skills/
    │   └── support_reply.py   Customer Support Reply skill
    └── kb/                    knowledge base (.md)
        ├── overview.md
        ├── features.md
        ├── pricing.md
        ├── enterprise.md
        ├── security.md
        ├── download.md
        ├── faq.md
        ├── contact.md
        ├── terms.md
        ├── privacy.md
        └── quick_reference.md
```

## Requirements

- Python `>=3.14`
- [`uv`](https://docs.astral.sh/uv/) for dependency management
- `OPENAI_API_KEY` environment variable

## Install

```bash
uv sync
```

This installs:
- `definable[serve]` — core agent framework + FastAPI/uvicorn for `agent.serve`
- `httpx[http2]`
- `numpy`

Transitively pulls: `openai`, `aiosqlite`, `pydantic`, `tiktoken`, `voyageai`, `fastapi`, `uvicorn`, `rich`, `prompt-toolkit`.

## Configure

Export your OpenAI key:

```bash
export OPENAI_API_KEY=sk-...
```

## Run

```bash
uv run python main.py
```

- Runs one demo query (`"What pricing plans does Luumen offer?"`) and prints the answer.
- Then starts the FastAPI server on the default port for further interaction.

Traces land in `./traces/<session_id>.jsonl`. Memory persists to `./memory.db`.

## Customise

- **Change the model** — edit `model="..."` in [app/agent.py](app/agent.py).
- **Update the KB** — drop new `.md` files into [app/kb/](app/kb/). Re-run to re-index.
- **Add a guardrail** — define it in [app/guardrails/custom.py](app/guardrails/custom.py) and wire it into [app/guardrails/config.py](app/guardrails/config.py).
- **Add a skill** — drop a new file in [app/skills/](app/skills/), export from `__init__.py`, add to `skills=[...]` in `agent.py`.
- **Tune security** — edit [app/security/config.py](app/security/config.py) (rate limit, tool allowlist, SSRF, etc.).

## Notes

- KB is re-embedded on every cold start because the default vector DB is in-memory. Swap for `qdrant`, `chroma`, `pgvector`, etc. (via `definable[<backend>]` extra) for persistence.
- The `customer_support_reply` skill was adapted from <https://www.skills.sh/eddiebe147/claude-settings/customer-support-reply>.
- KB content sourced from `www.luumen.ai` plus the internal customer-support knowledge document.
