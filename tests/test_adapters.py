import pytest
import warnings
from gpt_rosetta_stone.models import StandardRequest, Message
from gpt_rosetta_stone.adapters import OpenAIAdapter, ErnieAdapter, QwenAdapter


def test_openai_adapter():
    adapter = OpenAIAdapter()
    req = StandardRequest(
        model="gpt-4",
        messages=[Message(role="user", content="test")],
        temperature=0.7
    )
    result = adapter.transform_request(req)
    assert result["model"] == "gpt-4"
    assert result["temperature"] == 0.7


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
    assert "max_tokens" not in result


def test_ernie_adapter_temperature_transform():
    adapter = ErnieAdapter()
    req = StandardRequest(
        model="gpt-4",
        messages=[Message(role="user", content="test")],
        temperature=1.5
    )
    result = adapter.transform_request(req)
    assert result["temperature"] == 1.0  # 限制在 1.0


def test_ernie_adapter_unsupported_warning():
    adapter = ErnieAdapter()
    req = StandardRequest(
        model="gpt-4",
        messages=[Message(role="user", content="test")],
        frequency_penalty=0.5
    )
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        result = adapter.transform_request(req)
        assert len(w) == 1
        assert "frequency_penalty" in str(w[0].message)


def test_qwen_adapter():
    adapter = QwenAdapter()
    req = StandardRequest(
        model="gpt-4",
        messages=[Message(role="user", content="test")],
        max_tokens=100
    )
    result = adapter.transform_request(req)
    assert result["max_tokens"] == 100
