from transformers import pipeline
generator = pipeline('text-generation', model='gpt2-large')
print("Enter a prompt: ")
input = input()
print(generator(f"Generate possible outcomes that comes after '{input}' based on google search trends. The sentence should start with: {input} ___", max_length=100, truncation = True, num_return_sequences=5))


