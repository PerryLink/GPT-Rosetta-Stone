from typing import Dict, Any
from .base import BaseAdapter
from ..models import StandardRequest
from ..mappings.ernie_mappings import (
    ERNIE_PARAMETER_MAPPING,
    ERNIE_VALUE_TRANSFORMS,
    ERNIE_UNSUPPORTED,
)
import warnings


class ErnieAdapter(BaseAdapter):
    def transform_request(self, request: StandardRequest) -> Dict[str, Any]:
        result = {}
        request_dict = request.model_dump(exclude_none=True)

        for std_param, value in request_dict.items():
            if std_param in ERNIE_UNSUPPORTED:
                warnings.warn(f"参数 '{std_param}' 不被文心模型支持,已忽略")
                continue

            if std_param in ERNIE_PARAMETER_MAPPING:
                target_param = ERNIE_PARAMETER_MAPPING[std_param]
                if std_param in ERNIE_VALUE_TRANSFORMS:
                    value = ERNIE_VALUE_TRANSFORMS[std_param](value)
                result[target_param] = value

        return result

    def get_parameter_mapping(self) -> Dict[str, str]:
        return ERNIE_PARAMETER_MAPPING
