import pytest
from gpt_rosetta_stone.models import Message, StandardRequest


def test_message_creation():
    msg = Message(role="user", content="Hello")
    assert msg.role == "user"
    assert msg.content == "Hello"


def test_standard_request_minimal():
    req = StandardRequest(
        model="gpt-4",
        messages=[Message(role="user", content="test")]
    )
    assert req.model == "gpt-4"
    assert len(req.messages) == 1
    assert req.temperature == 0.7  # 默认值


def test_standard_request_with_params():
    req = StandardRequest(
        model="gpt-4",
        messages=[Message(role="user", content="test")],
        temperature=0.5,
        max_tokens=100
    )
    assert req.temperature == 0.5
    assert req.max_tokens == 100


def test_temperature_validation():
    with pytest.raises(Exception):
        StandardRequest(
            model="gpt-4",
            messages=[Message(role="user", content="test")],
            temperature=3.0  # 超出范围
        )
