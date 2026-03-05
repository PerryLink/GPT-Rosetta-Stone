"""基础使用示例"""
from gpt_rosetta_stone import RosettaStone

# 创建转换器,目标为文心模型
converter = RosettaStone(target_provider="ernie")

# 准备 OpenAI 格式的请求
request = {
    "model": "gpt-4",
    "messages": [{"role": "user", "content": "你好"}],
    "temperature": 0.7,
    "max_tokens": 100
}

# 转换为文心格式
result = converter.convert_request(request)

print("转换结果:")
print(result)
# 输出: {'model': 'gpt-4', 'messages': [{'role': 'user', 'content': '你好'}],
#        'temperature': 0.7, 'max_output_tokens': 100}
