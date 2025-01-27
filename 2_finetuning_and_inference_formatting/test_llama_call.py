import json
from llamaapi import LlamaAPI
from prompts import create_prompt
import os


llama = LlamaAPI(os.getenv("LLAMAAI_API_KEY"))

prompt = create_prompt(3)

api_request_json = {
    "model": "llama3.1-8b",
    "messages": [
        {"role": "system", "content": "provide a short,and precise response as if you are a university teacher. you will be penalized for verbose response"+prompt},
        {"role": "user", "content": "What is Tuned Oscillator Circuit?."},
    ],
    "max_tokens": 512,
}

# Execute the Request
response = llama.run(api_request_json)
print(response.json()["choices"][0]["message"]["content"])

