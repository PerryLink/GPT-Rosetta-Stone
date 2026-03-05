ERNIE_PARAMETER_MAPPING = {
    "model": "model",
    "messages": "messages",
    "temperature": "temperature",
    "top_p": "top_p",
    "max_tokens": "max_output_tokens",
    "stream": "stream",
    "presence_penalty": "penalty_score",
}

ERNIE_VALUE_TRANSFORMS = {
    "temperature": lambda x: max(0.01, min(1.0, x)),
    "top_p": lambda x: max(0.0, min(1.0, x)),
}

ERNIE_UNSUPPORTED = ["frequency_penalty", "n", "stop"]
