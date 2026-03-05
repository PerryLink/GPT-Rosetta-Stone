import pytest
from gpt_rosetta_stone import RosettaStone
from gpt_rosetta_stone.exceptions import UnsupportedProviderError


def test_rosetta_stone_openai():
    converter = RosettaStone(target_provider="openai")
    result = converter.convert_request({
        "model": "gpt-4",
        "messages": [{"role": "user", "content": "test"}],
        "temperature": 0.7
    })
    assert result["model"] == "gpt-4"
    assert result["temperature"] == 0.7


def test_rosetta_stone_ernie():
    converter = RosettaStone(target_provider="ernie")
    result = converter.convert_request({
        "model": "gpt-4",
        "messages": [{"role": "user", "content": "test"}],
        "max_tokens": 100
    })
    assert "max_output_tokens" in result
    assert result["max_output_tokens"] == 100


def test_rosetta_stone_unsupported_provider():
    with pytest.raises(UnsupportedProviderError):
        RosettaStone(target_provider="unknown")


def test_rosetta_stone_invalid_request():
    converter = RosettaStone(target_provider="openai")
    with pytest.raises(ValueError):
        converter.convert_request({
            "model": "gpt-4"
            # 缺少必需的 messages 字段
        })
