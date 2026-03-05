from typing import Dict, Any
from .base import BaseAdapter
from ..models import StandardRequest


class OpenAIAdapter(BaseAdapter):
    def transform_request(self, request: StandardRequest) -> Dict[str, Any]:
        """OpenAI 格式直通,无需转换"""
        return request.model_dump(exclude_none=True)

    def get_parameter_mapping(self) -> Dict[str, str]:
        return {
            "model": "model",
            "messages": "messages",
            "temperature": "temperature",
            "top_p": "top_p",
            "max_tokens": "max_tokens",
            "stream": "stream",
            "presence_penalty": "presence_penalty",
            "frequency_penalty": "frequency_penalty",
            "n": "n",
            "stop": "stop",
        }
