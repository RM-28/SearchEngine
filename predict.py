from transformers import BertTokenizer, BertForMaskedLM, BertModel
import torch

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')



text = "How to [MASK] [MASK]."
inputs = tokenizer(text, return_tensors='pt')


with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits


masked_index = torch.where(inputs['input_ids'][0] == tokenizer.mask_token_id)[0]


predicted_token_id = logits[0, masked_index].argmax(axis=-1)
predicted_token = tokenizer.decode(predicted_token_id)
print("What is", predicted_token)