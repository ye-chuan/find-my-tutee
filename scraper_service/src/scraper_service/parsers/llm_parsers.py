import requests
import tomllib
from pydantic import BaseModel, ValidationError

class LLMConfig(BaseModel):
    openai_endpoint: str
    model: str
    api_key: str

class AppConfig(BaseModel):
    llm: LLMConfig

config = {}
with open("config.toml", "rb") as f:
    config = tomllib.load(f)

try:
    config = AppConfig.model_validate(config)
except ValidationError:
    raise ValueError("Malformed LLM Config")

llm_config = config.llm
openai_endpoint = llm_config.openai_endpoint
model = llm_config.model

messages = [
    {"role": "user",
     "content": "Hello there, introduce yourself"}
]

payload = {
    "model": model,
    "messages": messages,

}
r = requests.post(openai_endpoint + "chat/completions", json=payload)

r_json = r.json()
r_json["choices"][0]

