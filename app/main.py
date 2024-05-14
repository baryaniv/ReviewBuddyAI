from fastapi import FastAPI
import tensorflow_hub as hub
import tensorflow as tf 

# Load the pre-trained Universal Sentence Encoder model from TensorFlow Hub.
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_embedding_for_text")
async def get_embedding(text: str):
    embeddings = embed([text])  # Pass the text as a list
    embeddings = embeddings.numpy()
    return {"embeddings": embeddings.tolist()}  # Convert embeddings to a list for JSON serialization