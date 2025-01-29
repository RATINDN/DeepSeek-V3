from flask import Flask, request, jsonify
import torch
from transformers import AutoTokenizer
from model import Transformer, ModelArgs
from generate import generate
import json
import os

app = Flask(__name__)

# Load model and tokenizer
ckpt_path = "./checkpoints"
config_path = "./config_671B.json"
with open(config_path) as f:
    args = ModelArgs(**json.load(f))
model = Transformer(args)
tokenizer = AutoTokenizer.from_pretrained(ckpt_path)
model.load_state_dict(torch.load(os.path.join(ckpt_path, "model0-mp1.safetensors")))

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    max_new_tokens = data.get('max_new_tokens', 100)
    temperature = data.get('temperature', 1.0)
    prompt_tokens = tokenizer.encode(prompt, return_tensors='pt').tolist()
    completion_tokens = generate(model, [prompt_tokens], max_new_tokens, tokenizer.eos_token_id, temperature)
    completion = tokenizer.decode(completion_tokens[0], skip_special_tokens=True)
    return jsonify({'completion': completion})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)