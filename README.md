<div align="center">

# GPT-Rosetta-Stone

**A unified API parameter conversion tool that translates OpenAI-format requests to Ernie (文心) and Qwen (通义).**

*Ported into [dsh-translate](https://github.com/PerryLink/dsh-translate) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

GPT-Rosetta-Stone converts OpenAI-format chat request parameters into the format expected by other LLM providers. It maps parameter names, clamps value ranges, and warns about unsupported parameters — all through one `RosettaStone` interface.

## Features

- **Unified interface** — convert between providers with a single `convert_request` call
- **Type safety** — Pydantic v2 request models validate input
- **Smart conversion** — automatic parameter mapping and value-range adjustment
- **Graceful handling** — friendly warnings for unsupported parameters
- **Extensible** — add a new provider in three steps (adapter + mapping + factory entry)

## Quick start

```bash
pip install gpt-rosetta-stone
```

```python
from gpt_rosetta_stone import RosettaStone

converter = RosettaStone(target_provider="ernie")
result = converter.convert_request({
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你好"}],
    "temperature": 0.7,
    "max_tokens": 100,
})
print(result)
# {'model': 'gpt-4', 'messages': [...], 'temperature': 0.7, 'max_output_tokens': 100}
```

## Usage

### Supported providers

| Provider | Status | Notes |
|----------|--------|-------|
| OpenAI | ✅ Supported | Standard format (passthrough) |
| Ernie (文心) | ✅ Supported | Baidu Wenxin LLM |
| Qwen (通义) | ✅ Supported | Alibaba Qwen |

### Parameter mapping

**Ernie (文心)**

| OpenAI parameter | Ernie parameter | Notes |
|------------------|-----------------|-------|
| `max_tokens` | `max_output_tokens` | Maximum output tokens |
| `presence_penalty` | `penalty_score` | Presence penalty |
| `temperature` | `temperature` | Range limited to 0.01–1.0 |
| `frequency_penalty` | ❌ Not supported | Warning issued |

**Qwen (通义)**

| OpenAI parameter | Qwen parameter | Notes |
|------------------|----------------|-------|
| `max_tokens` | `max_tokens` | Same |
| `presence_penalty` | `presence_penalty` | Same |
| `frequency_penalty` | ❌ Not supported | Warning issued |

### CLI

```bash
# Convert from a file
gpt-rosetta-stone convert --target ernie --input request.json

# Convert inline JSON
gpt-rosetta-stone convert --target ernie --data '{"model":"gpt-4","messages":[{"role":"user","content":"test"}]}'

# Show the parameter mapping for a provider
gpt-rosetta-stone show-mapping --provider ernie
```

## Development

```bash
poetry install
poetry run pytest tests/ -v
poetry run black src/ tests/
poetry run ruff check src/ tests/
```

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
