from transformers import AutoTokenizer, AutoModel
import torch

# Load the pre-trained model and tokenizer
model_name = "HuggingFaceH4/zephyr-7b-beta"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Prepare your text
text = "Food is amazing, and the service is even better!"

# Tokenize the text
inputs = tokenizer(text, return_tensors="pt")

# Generate embeddings
with torch.no_grad():
    outputs = model(**inputs)

# Extract the embeddings
embeddings = outputs.last_hidden_state[:, 0, :].numpy()

print(embeddings)