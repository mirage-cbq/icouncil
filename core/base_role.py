"""
AI Council — 角色基类
所有角色继承此类，统一管理模型调用、工具调用和输出格式
"""

from abc import ABC, abstractmethod
from typing import Optional
import yaml


class BaseRole(ABC):
    """
    所有评议角色的基类
    子类只需实现 system_prompt 属性和 parse_output 方法
    """

    def __init__(self, config: dict, tools: Optional[list] = None):
        self.config = config
        self.tools = tools or []
        self.model = config.get("model", "claude-sonnet-4-20250514")
        self.temperature = config.get("temperature", 0.5)
        self.max_tokens = config.get("max_tokens", 2000)

    @property
    @abstractmethod
    def system_prompt(self) -> str:
        """每个角色定义自己的系统提示词"""
        pass

    @abstractmethod
    def parse_output(self, raw_output: str) -> dict:
        """将模型输出解析为结构化数据"""
        pass

    def build_messages(self, user_content: str, history: Optional[list] = None) -> list:
        """构建发送给模型的消息列表"""
        messages = history or []
        messages.append({"role": "user", "content": user_content})
        return messages

    def run(self, input_content: str, history: Optional[list] = None) -> dict:
        """
        调用模型，返回解析后的结构化结果
        实际调用逻辑由 LLMClient 注入，这里定义接口
        """
        raise NotImplementedError("需要注入 LLMClient 后调用")


class LLMClient:
    """
    模型调用客户端
    封装不同厂商API的调用差异，对上层角色透明
    支持：Anthropic Claude / OpenAI / 本地Ollama
    """

    def __init__(self, provider: str, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.provider = provider      # "anthropic" / "openai" / "ollama"
        self.api_key = api_key
        self.base_url = base_url      # 本地模型用

    def call(
        self,
        model: str,
        system_prompt: str,
        messages: list,
        temperature: float,
        max_tokens: int,
        tools: Optional[list] = None
    ) -> str:
        """
        统一的模型调用入口
        返回模型的文本输出
        """
        if self.provider == "anthropic":
            return self._call_anthropic(model, system_prompt, messages, temperature, max_tokens, tools)
        elif self.provider == "openai":
            return self._call_openai(model, system_prompt, messages, temperature, max_tokens, tools)
        elif self.provider == "ollama":
            return self._call_ollama(model, system_prompt, messages, temperature, max_tokens)
        else:
            raise ValueError(f"不支持的模型提供商: {self.provider}")

    def _call_anthropic(self, model, system_prompt, messages, temperature, max_tokens, tools):
        # TODO: 实现 Anthropic API 调用
        raise NotImplementedError

    def _call_openai(self, model, system_prompt, messages, temperature, max_tokens, tools):
        # TODO: 实现 OpenAI 兼容 API 调用（也覆盖本地 LM Studio / vLLM）
        raise NotImplementedError

    def _call_ollama(self, model, system_prompt, messages, temperature, max_tokens):
        # TODO: 实现 Ollama 本地调用
        raise NotImplementedError
