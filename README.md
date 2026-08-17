<div align="center">

# GPT-Rosetta-Stone

**A unified API parameter conversion tool for large language models, supporting OpenAI, Ernie (文心), Qwen (通义) and more.**

*Ported into [dsh-translate](https://github.com/PerryLink/dsh-translate) — part of the PerryLink DSH Plugin Family.*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## What it does

GPT-Rosetta-Stone converts OpenAI-format chat request parameters into the format expected by other LLM providers. It maps parameter names, clamps value ranges, and warns about unsupported parameters — all through a single `RosettaStone` interface.

## Features

- **Unified interface** — convert between different LLM provider APIs with a single interface
- **Type safety** — built with Pydantic v2 for robust data validation
- **Extensible** — add new providers in just 3 steps
- **Smart conversion** — automatic parameter mapping and value-range adjustment
- **Graceful handling** — friendly warnings for unsupported parameters
- **CLI support** — command-line interface with Rich output

## Quick start

```bash
# Using pip
pip install gpt-rosetta-stone

# Using Poetry
poetry add gpt-rosetta-stone
```

### Basic usage

```python
from gpt_rosetta_stone import RosettaStone

# Create converter for Ernie (Baidu)
converter = RosettaStone(target_provider="ernie")

# Convert OpenAI-format request
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
# Convert from file
gpt-rosetta-stone convert --target ernie --input request.json

# Convert inline JSON
gpt-rosetta-stone convert --target ernie --data '{"model":"gpt-4","messages":[{"role":"user","content":"test"}]}'

# Show the parameter mapping for a provider
gpt-rosetta-stone show-mapping --provider ernie
```

### API reference

**`RosettaStone`** — main conversion class.

```python
converter = RosettaStone(target_provider="ernie")
result = converter.convert_request(request_data)
```

- `target_provider` (str): target provider name (`"openai"`, `"ernie"`, `"qwen"`)
- `convert_request(request_data: Dict) -> Dict`: convert request parameters

**`StandardRequest`** — standard request model (OpenAI-compatible).

| Field | Type | Description |
|-------|------|-------------|
| `model` | str | Model name |
| `messages` | List[Message] | Message list |
| `temperature` | float, optional | Sampling temperature, default `0.7` |
| `top_p` | float, optional | Nucleus sampling probability, default `1.0` |
| `max_tokens` | int, optional | Maximum output tokens |
| `stream` | bool, optional | Stream output, default `False` |
| `presence_penalty` | float, optional | Presence penalty, default `0` |
| `frequency_penalty` | float, optional | Frequency penalty, default `0` |
| `n` | int, optional | Number of results, default `1` |
| `stop` | List[str], optional | Stop sequences |

## Extending

Adding a new model provider requires only 3 steps:

1. Create adapter — `src/gpt_rosetta_stone/adapters/newprovider.py`
2. Create mapping — `src/gpt_rosetta_stone/mappings/newprovider_mappings.py`
3. Register in factory — add an entry in `AdapterFactory.ADAPTERS`

## Tech stack

| Component | Library |
|-----------|---------|
| Programming language | Python 3.8+ |
| Data validation | Pydantic 2.0+ |
| CLI framework | Click 8.1+ |
| Terminal formatting | Rich 13.0+ |
| Configuration files | PyYAML 6.0+ |
| Testing | Pytest 8.0+ |
| Code formatting | Black 24.0+ |
| Code linting | Ruff 0.3+ |

## Development

```bash
poetry install
poetry run pytest tests/ -v
poetry run black src/ tests/
poetry run ruff check src/ tests/
```

## Related

- [dsh-translate](https://github.com/PerryLink/dsh-translate) — the DSH plugin this project was ported into
- [PerryLink](https://github.com/PerryLink) — the PerryLink DSH plugin family

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

[Apache License 2.0](LICENSE) © 2026 PerryLink
