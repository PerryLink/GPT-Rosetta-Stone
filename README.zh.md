<div align="center">

# GPT-Rosetta-Stone

**统一的大模型 API 参数转换工具，支持 OpenAI、文心（Ernie）、通义（Qwen）等多家提供商。**

*已移植至 [dsh-translate](https://github.com/PerryLink/dsh-translate) —— 属于 PerryLink DSH 插件家族。*

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)

[English](README.md) · [简体中文](README.zh.md)

</div>

---

## 功能简介

GPT-Rosetta-Stone 将 OpenAI 格式的对话请求参数转换为其他 LLM 提供商所需的格式。它会映射参数名、调整取值范围，并对不支持的参数给出提示——全部通过统一的 `RosettaStone` 接口完成。

## 核心特性

- **统一接口** —— 通过单一接口在不同 LLM 提供商 API 之间转换
- **类型安全** —— 基于 Pydantic v2 构建，稳健的数据校验
- **易于扩展** —— 仅需 3 步即可添加新提供商
- **智能转换** —— 自动映射参数并调整取值范围
- **友好处理** —— 对不支持的参数给出友好警告
- **CLI 支持** —— 带 Rich 输出的命令行界面

## 快速开始

```bash
# 使用 pip
pip install gpt-rosetta-stone

# 使用 Poetry
poetry add gpt-rosetta-stone
```

### 基本使用

```python
from gpt_rosetta_stone import RosettaStone

# 创建文心（百度）模型转换器
converter = RosettaStone(target_provider="ernie")

# 转换 OpenAI 格式请求
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
# 从文件转换
gpt-rosetta-stone convert --target ernie --input request.json

# 转换内联 JSON
gpt-rosetta-stone convert --target ernie --data '{"model":"gpt-4","messages":[{"role":"user","content":"test"}]}'

# 查看某提供商的参数映射
gpt-rosetta-stone show-mapping --provider ernie
```

### API 参考

**`RosettaStone`** —— 主转换类。

```python
converter = RosettaStone(target_provider="ernie")
result = converter.convert_request(request_data)
```

- `target_provider` (str)：目标提供商名称（`"openai"`、`"ernie"`、`"qwen"`）
- `convert_request(request_data: Dict) -> Dict`：转换请求参数

**`StandardRequest`** —— 标准请求模型（兼容 OpenAI 格式）。

| 字段 | 类型 | 说明 |
|------|------|------|
| `model` | str | 模型名称 |
| `messages` | List[Message] | 消息列表 |
| `temperature` | float，可选 | 采样温度，默认 `0.7` |
| `top_p` | float，可选 | 核采样概率，默认 `1.0` |
| `max_tokens` | int，可选 | 最大输出 token 数 |
| `stream` | bool，可选 | 流式输出，默认 `False` |
| `presence_penalty` | float，可选 | 存在惩罚，默认 `0` |
| `frequency_penalty` | float，可选 | 频率惩罚，默认 `0` |
| `n` | int，可选 | 结果数量，默认 `1` |
| `stop` | List[str]，可选 | 停止序列 |

## 扩展

添加新的模型提供商只需 3 步：

1. 创建适配器 —— `src/gpt_rosetta_stone/adapters/newprovider.py`
2. 创建映射 —— `src/gpt_rosetta_stone/mappings/newprovider_mappings.py`
3. 注册到工厂 —— 在 `AdapterFactory.ADAPTERS` 中添加条目

## 技术栈

| 组件 | 库 |
|------|----|
| 编程语言 | Python 3.8+ |
| 数据校验 | Pydantic 2.0+ |
| CLI 框架 | Click 8.1+ |
| 终端格式化 | Rich 13.0+ |
| 配置文件 | PyYAML 6.0+ |
| 测试框架 | Pytest 8.0+ |
| 代码格式化 | Black 24.0+ |
| 代码检查 | Ruff 0.3+ |

## 开发

```bash
poetry install
poetry run pytest tests/ -v
poetry run black src/ tests/
poetry run ruff check src/ tests/
```

## 相关项目

- [dsh-translate](https://github.com/PerryLink/dsh-translate) —— 本项目被移植进的 DSH 插件
- [PerryLink](https://github.com/PerryLink) —— PerryLink DSH 插件家族

## 贡献

欢迎贡献！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

## 许可证

[Apache License 2.0](LICENSE) © 2026 PerryLink
