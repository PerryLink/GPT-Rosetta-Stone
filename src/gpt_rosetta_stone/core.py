from typing import Dict, Any
from .models import StandardRequest
from .adapters.factory import AdapterFactory
from pydantic import ValidationError


class RosettaStone:
    def __init__(self, target_provider: str):
        self.target_provider = target_provider
        self.adapter = AdapterFactory.get_adapter(target_provider)

    def convert_request(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """转换请求参数"""
        try:
            standard_request = StandardRequest(**request_data)
            transformed = self.adapter.transform_request(standard_request)
            return transformed
        except ValidationError as e:
            raise ValueError(f"请求参数验证失败: {e}")
