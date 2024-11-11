
import re
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained GPT-2 model and tokenizer
model_name = "gpt2-large"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

model.eval()

def generate_response(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)
    prediction = tokenizer.decode(output[0], skip_special_tokens=True)

    return prediction

while True:
    print("Enter a prompt: ")
    prompt = input()
    if prompt == "exit":
        break
    else:
        answer = generate_response(f"Finish the sentence from google trends search engine based on the sentence: {prompt}")
        print()
 