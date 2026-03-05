from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class Message(BaseModel):
    role: str = Field(..., description="消息角色: system, user, assistant")
    content: str = Field(..., description="消息内容")


class StandardRequest(BaseModel):
    model: str = Field(..., description="模型名称")
    messages: List[Message] = Field(..., description="对话消息列表")
    temperature: Optional[float] = Field(default=0.7, ge=0, le=2, description="采样温度")
    top_p: Optional[float] = Field(default=1.0, ge=0, le=1, description="核采样概率")
    max_tokens: Optional[int] = Field(default=None, ge=1, description="最大生成token数")
    stream: Optional[bool] = Field(default=False, description="是否流式输出")
    presence_penalty: Optional[float] = Field(default=0, ge=-2, le=2, description="存在惩罚")
    frequency_penalty: Optional[float] = Field(default=0, ge=-2, le=2, description="频率惩罚")
    n: Optional[int] = Field(default=1, ge=1, description="生成结果数量")
    stop: Optional[List[str]] = Field(default=None, description="停止词列表")


class StandardResponse(BaseModel):
    id: str
    model: str
    choices: List[Dict[str, Any]]
    usage: Optional[Dict[str, int]] = None
