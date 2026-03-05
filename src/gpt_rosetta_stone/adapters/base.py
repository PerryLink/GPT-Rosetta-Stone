from abc import ABC, abstractmethod
from typing import Dict, Any
from ..models import StandardRequest


class BaseAdapter(ABC):
    @abstractmethod
    def transform_request(self, request: StandardRequest) -> Dict[str, Any]:
        """将标准请求转换为目标提供商格式"""
        pass

    @abstractmethod
    def get_parameter_mapping(self) -> Dict[str, str]:
        """返回参数映射字典"""
        pass
