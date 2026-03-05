# GPT Rosetta Stone

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Apache%202.0-green.svg)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**A unified API parameter conversion tool for large language models, supporting OpenAI, Ernie, Qwen and more.**

**统一的大模型 API 参数转换工具,支持 OpenAI、文心、通义等多家提供商。**

---

## ✨ Features | 核心特性

- 🔄 **Unified Interface** - Convert between different LLM provider APIs with a single interface | 统一接口,一键转换不同提供商的 API 参数
- 🎯 **Type Safety** - Built with Pydantic v2 for robust data validation | 基于 Pydantic v2 的类型安全验证
- 🔌 **Extensible** - Add new providers in just 3 steps | 仅需 3 步即可添加新提供商
- ⚡ **Smart Conversion** - Automatic parameter mapping and value range adjustment | 智能参数映射和值范围自动调整
- 🛡️ **Graceful Handling** - Friendly warnings for unsupported parameters | 不支持参数的友好警告机制
- 🎨 **CLI Support** - Beautiful command-line interface with rich output | 美观的命令行界面

---

## 🚀 Quick Start | 快速开始

### Installation | 安装

```bash
# Using pip
pip install gpt-rosetta-stone

# Using Poetry
poetry add gpt-rosetta-stone
```

### Basic Usage | 基础使用

```python
from gpt_rosetta_stone import RosettaStone

# Create converter for Ernie (Baidu) | 创建文心模型转换器
converter = RosettaStone(target_provider="ernie")

# Convert OpenAI format request | 转换 OpenAI 格式请求
result = converter.convert_request({
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你好"}],
    "temperature": 0.7,
    "max_tokens": 100
})

print(result)
# Output: {'model': 'gpt-4', 'messages': [...], 'temperature': 0.7, 'max_output_tokens': 100}
```

---

## 📖 Usage Guide | 使用指南

### Supported Providers | 支持的提供商

| Provider | Status | Notes |
|----------|--------|-------|
| **OpenAI** | ✅ Supported | Standard format (passthrough) |
| **Ernie (文心)** | ✅ Supported | Baidu Wenxin LLM |
| **Qwen (通义)** | ✅ Supported | Alibaba Qwen |

### Parameter Mapping | 参数映射

#### Ernie (文心)

| OpenAI Parameter | Ernie Parameter | Notes |
|-----------------|-----------------|-------|
| `max_tokens` | `max_output_tokens` | Maximum output tokens |
| `presence_penalty` | `penalty_score` | Presence penalty |
| `temperature` | `temperature` | Range limited to 0.01-1.0 |
| `frequency_penalty` | ❌ Not supported | Warning issued |

#### Qwen (通义)

| OpenAI Parameter | Qwen Parameter | Notes |
|-----------------|----------------|-------|
| `max_tokens` | `max_tokens` | Same |
| `presence_penalty` | `presence_penalty` | Same |
| `frequency_penalty` | ❌ Not supported | Warning issued |

### CLI Usage | 命令行使用

#### Convert Request | 转换请求

```bash
# From file | 从文件读取
gpt-rosetta-stone convert --target ernie --input request.json

# Direct JSON input | 直接传入 JSON
gpt-rosetta-stone convert --target ernie --data '{"model":"gpt-4","messages":[{"role":"user","content":"test"}]}'
```

#### Show Parameter Mapping | 查看参数映射

```bash
gpt-rosetta-stone show-mapping --provider ernie
```

### API Reference | API 参考

#### `RosettaStone`

Main conversion class | 主转换类

```python
converter = RosettaStone(target_provider="ernie")
result = converter.convert_request(request_data)
```

**Parameters | 参数:**
- `target_provider` (str): Target provider name ("openai", "ernie", "qwen")

**Methods | 方法:**
- `convert_request(request_data: Dict) -> Dict`: Convert request parameters

#### `StandardRequest`

Standard request model (OpenAI compatible) | 标准请求模型(兼容 OpenAI 格式)

**Fields | 字段:**
- `model` (str): Model name
- `messages` (List[Message]): Message list
- `temperature` (float, optional): Sampling temperature, default 0.7
- `top_p` (float, optional): Nucleus sampling probability, default 1.0
- `max_tokens` (int, optional): Maximum output tokens
- `stream` (bool, optional): Stream output, default False
- `presence_penalty` (float, optional): Presence penalty, default 0
- `frequency_penalty` (float, optional): Frequency penalty, default 0
- `n` (int, optional): Number of results, default 1
- `stop` (List[str], optional): Stop sequences

---

## 📁 Project Structure | 项目结构

```
gpt-rosetta-stone/
├── src/gpt_rosetta_stone/
│   ├── __init__.py           # Package entry
│   ├── models.py             # Pydantic data models
│   ├── core.py               # Core conversion logic
│   ├── cli.py                # CLI interface
│   ├── exceptions.py         # Custom exceptions
│   ├── adapters/             # Adapter modules
│   │   ├── base.py           # Base adapter interface
│   │   ├── openai.py         # OpenAI adapter
│   │   ├── ernie.py          # Ernie adapter
│   │   ├── qwen.py           # Qwen adapter
│   │   └── factory.py        # Adapter factory
│   └── mappings/             # Parameter mapping configs
│       ├── ernie_mappings.py # Ernie mapping rules
│       └── qwen_mappings.py  # Qwen mapping rules
├── tests/                    # Test files
├── examples/                 # Example code
├── pyproject.toml            # Poetry configuration
└── README.md                 # Project documentation
```

---

## 🛠️ Technology Stack | 技术栈

- **Python 3.8+** - Programming language
- **Pydantic 2.0+** - Data validation and modeling
- **Click 8.1+** - CLI framework
- **Rich 13.0+** - Terminal formatting
- **PyYAML 6.0+** - Configuration file support
- **Pytest 8.0+** - Testing framework
- **Black 24.0+** - Code formatting
- **Ruff 0.3+** - Code linting

---

## 🔧 Development | 开发

### Install Dependencies | 安装依赖

```bash
poetry install
```

### Run Tests | 运行测试

```bash
poetry run pytest tests/ -v
```

### Code Formatting | 代码格式化

```bash
poetry run black src/ tests/
poetry run ruff check src/ tests/
```

---

## 🚀 Extending | 扩展

Adding a new model provider requires only 3 steps | 添加新的模型提供商只需 3 步:

1. Create adapter | 创建适配器: `src/gpt_rosetta_stone/adapters/newprovider.py`
2. Create mapping | 创建映射: `src/gpt_rosetta_stone/mappings/newprovider_mappings.py`
3. Register in factory | 注册到工厂: Add entry in `AdapterFactory.ADAPTERS`

---

## 📄 License | 许可证

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

---

## 🤝 Contributing | 贡献

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📮 Contact | 联系方式

- GitHub: [@PerryLink](https://github.com/PerryLink)
- Email: novelnexusai@outlook.com

---

**Made with ❤️ by Chance Dean**
