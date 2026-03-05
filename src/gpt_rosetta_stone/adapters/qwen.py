from typing import Dict, Any
from .base import BaseAdapter
from ..models import StandardRequest
from ..mappings.qwen_mappings import (
    QWEN_PARAMETER_MAPPING,
    QWEN_VALUE_TRANSFORMS,
    QWEN_UNSUPPORTED,
)
import warnings


class QwenAdapter(BaseAdapter):
    def transform_request(self, request: StandardRequest) -> Dict[str, Any]:
        result = {}
        request_dict = request.model_dump(exclude_none=True)

        for std_param, value in request_dict.items():
            if std_param in QWEN_UNSUPPORTED:
                warnings.warn(f"参数 '{std_param}' 不被通义模型支持,已忽略")
                continue

            if std_param in QWEN_PARAMETER_MAPPING:
                target_param = QWEN_PARAMETER_MAPPING[std_param]
                if std_param in QWEN_VALUE_TRANSFORMS:
                    value = QWEN_VALUE_TRANSFORMS[std_param](value)
                result[target_param] = value

        return result

    def get_parameter_mapping(self) -> Dict[str, str]:
        return QWEN_PARAMETER_MAPPING
