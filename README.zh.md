<div align="center">

# GPT-Rosetta-Stone

**统一的大模型 API 参数转换工具，将 OpenAI 格式请求转换为文心（Ernie）和通义（Qwen）格式。**

*已移植至 [dsh-translate](https://github.com/PerryLink/dsh-translate) —— 属于 PerryLink DSH 插件家族。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

GPT-Rosetta-Stone 将 OpenAI 格式的对话请求参数转换为其他 LLM 提供商所需的格式。它会映射参数名、调整取值范围，并对不支持的参数给出提示——全部通过统一的 `RosettaStone` 接口完成。

## 核心特性

- **统一接口** —— 通过一次 `convert_request` 调用即可在不同提供商之间转换
- **类型安全** —— 基于 Pydantic v2 的请求模型校验输入
- **智能转换** —— 自动映射参数并调整取值范围
- **友好处理** —— 对不支持的参数给出友好警告
- **易于扩展** —— 三步即可添加新提供商（适配器 + 映射 + 工厂注册）

## 快速开始

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

## 使用指南

### 支持的提供商

| 提供商 | 状态 | 说明 |
|--------|------|------|
| OpenAI | ✅ 支持 | 标准格式（直通） |
| 文心（Ernie） | ✅ 支持 | 百度文心大模型 |
| 通义（Qwen） | ✅ 支持 | 阿里通义大模型 |

### 参数映射

**文心（Ernie）**

| OpenAI 参数 | 文心参数 | 说明 |
|-------------|----------|------|
| `max_tokens` | `max_output_tokens` | 最大输出 token 数 |
| `presence_penalty` | `penalty_score` | 存在惩罚 |
| `temperature` | `temperature` | 取值范围限制为 0.01–1.0 |
| `frequency_penalty` | ❌ 不支持 | 发出警告 |

**通义（Qwen）**

| OpenAI 参数 | 通义参数 | 说明 |
|-------------|----------|------|
| `max_tokens` | `max_tokens` | 相同 |
| `presence_penalty` | `presence_penalty` | 相同 |
| `frequency_penalty` | ❌ 不支持 | 发出警告 |

### 命令行

```bash
# 从文件读取
gpt-rosetta-stone convert --target ernie --input request.json

# 直接传入 JSON
gpt-rosetta-stone convert --target ernie --data '{"model":"gpt-4","messages":[{"role":"user","content":"test"}]}'

# 查看某提供商的参数映射
gpt-rosetta-stone show-mapping --provider ernie
```

## 开发

```bash
poetry install
poetry run pytest tests/ -v
poetry run black src/ tests/
poetry run ruff check src/ tests/
```

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
