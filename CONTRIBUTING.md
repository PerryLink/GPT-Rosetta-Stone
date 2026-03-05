# Contributing to GPT Rosetta Stone

# 贡献指南

Thank you for your interest in contributing to GPT Rosetta Stone!

感谢您对 GPT Rosetta Stone 项目的关注!

---

## Project Status | 项目状态

This is currently a **personal project** maintained by Chance Dean ([@PerryLink](https://github.com/PerryLink)). While contributions are welcome, please note that this project is primarily developed and maintained by a single person.

这是一个**个人维护项目**,由 Chance Dean ([@PerryLink](https://github.com/PerryLink)) 维护。虽然欢迎贡献,但请注意这个项目主要由个人开发和维护。

---

## How to Report Issues | 如何报告问题

If you encounter a bug or have a feature request, please:

如果您遇到 bug 或有功能建议,请:

1. **Check existing issues** - Search the [issue tracker](https://github.com/PerryLink/gpt-rosetta-stone/issues) to see if the issue has already been reported.

   **检查现有问题** - 在 [issue tracker](https://github.com/PerryLink/gpt-rosetta-stone/issues) 中搜索是否已有相关问题。

2. **Create a new issue** - If your issue is new, create a detailed issue report including:
   - Clear description of the problem or feature request
   - Steps to reproduce (for bugs)
   - Expected vs actual behavior
   - Your environment (Python version, OS, etc.)
   - Relevant code snippets or error messages

   **创建新问题** - 如果是新问题,请创建详细的问题报告,包括:
   - 问题或功能请求的清晰描述
   - 重现步骤(针对 bug)
   - 期望行为 vs 实际行为
   - 您的环境(Python 版本、操作系统等)
   - 相关代码片段或错误信息

---

## Development Environment Setup | 开发环境搭建

### Prerequisites | 前置要求

- Python 3.8 or higher | Python 3.8 或更高版本
- Poetry (recommended) or pip | Poetry(推荐)或 pip
- Git

### Setup Steps | 搭建步骤

1. **Fork and clone the repository | Fork 并克隆仓库**

   ```bash
   git clone https://github.com/YOUR_USERNAME/gpt-rosetta-stone.git
   cd gpt-rosetta-stone
   ```

2. **Install dependencies | 安装依赖**

   Using Poetry (recommended) | 使用 Poetry(推荐):
   ```bash
   poetry install
   ```

   Using pip | 使用 pip:
   ```bash
   pip install -e ".[dev]"
   ```

3. **Verify installation | 验证安装**

   ```bash
   # Run tests | 运行测试
   poetry run pytest tests/ -v

   # Check code style | 检查代码风格
   poetry run black --check src/ tests/
   poetry run ruff check src/ tests/
   ```

---

## Code Standards | 代码规范

### Style Guide | 代码风格

This project follows **PEP 8** - the official Python style guide.

本项目遵循 **PEP 8** - Python 官方代码风格指南。

Key points | 关键要点:

- **Line length**: Maximum 100 characters | **行长度**: 最多 100 字符
- **Indentation**: 4 spaces (no tabs) | **缩进**: 4 个空格(不使用 tab)
- **Naming conventions** | **命名规范**:
  - Functions and variables: `snake_case`
  - Classes: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
- **Imports**: Organized in three groups (standard library, third-party, local) | **导入**: 分为三组(标准库、第三方库、本地模块)

### Code Formatting | 代码格式化

We use **Black** for automatic code formatting:

我们使用 **Black** 进行自动代码格式化:

```bash
# Format code | 格式化代码
poetry run black src/ tests/

# Check formatting | 检查格式
poetry run black --check src/ tests/
```

### Linting | 代码检查

We use **Ruff** for fast Python linting:

我们使用 **Ruff** 进行快速 Python 代码检查:

```bash
# Run linter | 运行检查
poetry run ruff check src/ tests/

# Auto-fix issues | 自动修复问题
poetry run ruff check --fix src/ tests/
```

### Type Hints | 类型提示

- Use type hints for function parameters and return values | 为函数参数和返回值添加类型提示
- Leverage Pydantic models for data validation | 使用 Pydantic 模型进行数据验证

Example | 示例:
```python
from typing import Dict, Any
from gpt_rosetta_stone.models import StandardRequest

def convert_request(request: StandardRequest) -> Dict[str, Any]:
    """Convert request to target format."""
    ...
```

---

## Testing | 测试

### Running Tests | 运行测试

```bash
# Run all tests | 运行所有测试
poetry run pytest tests/ -v

# Run with coverage | 运行并生成覆盖率报告
poetry run pytest tests/ --cov=gpt_rosetta_stone --cov-report=html

# Run specific test file | 运行特定测试文件
poetry run pytest tests/test_adapters.py -v
```

### Writing Tests | 编写测试

- Place tests in the `tests/` directory | 将测试放在 `tests/` 目录
- Name test files with `test_` prefix | 测试文件以 `test_` 开头
- Name test functions with `test_` prefix | 测试函数以 `test_` 开头
- Aim for high test coverage (>80%) | 追求高测试覆盖率(>80%)

Example | 示例:
```python
def test_ernie_adapter_parameter_mapping():
    adapter = ErnieAdapter()
    req = StandardRequest(
        model="gpt-4",
        messages=[Message(role="user", content="test")],
        max_tokens=100
    )
    result = adapter.transform_request(req)
    assert "max_output_tokens" in result
    assert result["max_output_tokens"] == 100
```

---

## Pull Request Process | 提交 Pull Request 流程

### Before Submitting | 提交前

1. **Create a feature branch** | **创建功能分支**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** | **进行修改**
   - Write clean, well-documented code | 编写清晰、有良好文档的代码
   - Add tests for new functionality | 为新功能添加测试
   - Update documentation if needed | 如需要更新文档

3. **Run quality checks** | **运行质量检查**
   ```bash
   # Format code | 格式化代码
   poetry run black src/ tests/

   # Run linter | 运行检查
   poetry run ruff check src/ tests/

   # Run tests | 运行测试
   poetry run pytest tests/ -v
   ```

4. **Commit your changes** | **提交更改**
   ```bash
   git add .
   git commit -m "feat: add support for new provider"
   ```

   Use conventional commit messages | 使用约定式提交信息:
   - `feat:` - New feature | 新功能
   - `fix:` - Bug fix | Bug 修复
   - `docs:` - Documentation changes | 文档更改
   - `test:` - Test additions/changes | 测试添加/更改
   - `refactor:` - Code refactoring | 代码重构
   - `style:` - Code style changes | 代码风格更改

### Submitting | 提交

1. **Push to your fork** | **推送到您的 fork**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** | **创建 Pull Request**
   - Go to the original repository | 访问原始仓库
   - Click "New Pull Request" | 点击 "New Pull Request"
   - Select your branch | 选择您的分支
   - Fill in the PR template with:
     - Clear description of changes | 清晰的更改描述
     - Related issue numbers (if any) | 相关问题编号(如有)
     - Testing performed | 已执行的测试
     - Screenshots (if applicable) | 截图(如适用)

3. **Wait for review** | **等待审查**
   - The maintainer will review your PR | 维护者会审查您的 PR
   - Address any feedback or requested changes | 处理任何反馈或请求的更改
   - Once approved, your PR will be merged | 批准后,您的 PR 将被合并

---

## Adding New Providers | 添加新提供商

To add support for a new LLM provider, follow these steps:

要添加对新 LLM 提供商的支持,请按以下步骤操作:

1. **Create adapter** | **创建适配器**
   - File: `src/gpt_rosetta_stone/adapters/newprovider.py`
   - Inherit from `BaseAdapter`
   - Implement `transform_request()` and `get_parameter_mapping()`

2. **Create mapping** | **创建映射**
   - File: `src/gpt_rosetta_stone/mappings/newprovider_mappings.py`
   - Define parameter mapping dictionary
   - Define value transformation functions
   - List unsupported parameters

3. **Register in factory** | **在工厂中注册**
   - Update `AdapterFactory.ADAPTERS` in `adapters/factory.py`

4. **Add tests** | **添加测试**
   - Create test cases in `tests/test_adapters.py`
   - Test parameter mapping, value transforms, and warnings

5. **Update documentation** | **更新文档**
   - Add provider to README.md
   - Document parameter mappings

---

## Questions? | 有疑问?

If you have any questions about contributing, feel free to:

如果您对贡献有任何疑问,请随时:

- Open an issue for discussion | 开启一个 issue 进行讨论
- Contact the maintainer: novelnexusai@outlook.com | 联系维护者: novelnexusai@outlook.com

---

## Code of Conduct | 行为准则

- Be respectful and inclusive | 保持尊重和包容
- Provide constructive feedback | 提供建设性反馈
- Focus on what is best for the project | 关注对项目最有利的事情
- Show empathy towards other contributors | 对其他贡献者表示同理心

---

**Thank you for contributing! | 感谢您的贡献!** 🎉
