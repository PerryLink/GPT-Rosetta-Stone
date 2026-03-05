from .base import BaseAdapter
from .openai import OpenAIAdapter
from .ernie import ErnieAdapter
from .qwen import QwenAdapter
from ..exceptions import UnsupportedProviderError


class AdapterFactory:
    ADAPTERS = {
        "openai": OpenAIAdapter,
        "ernie": ErnieAdapter,
        "qwen": QwenAdapter,
    }

    @staticmethod
    def get_adapter(provider: str) -> BaseAdapter:
        """根据提供商名称返回对应适配器"""
        provider = provider.lower()
        if provider not in AdapterFactory.ADAPTERS:
            raise UnsupportedProviderError(
                f"不支持的提供商: {provider}. 支持的提供商: {list(AdapterFactory.ADAPTERS.keys())}"
            )
        return AdapterFactory.ADAPTERS[provider]()
