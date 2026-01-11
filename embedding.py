from ollama import Client
import ollama
from dotenv import load_dotenv
import os
load_dotenv()
def generateEmbedding(question):
    embedding = ollama.embed(
        model='embeddinggemma',
        input=question
    )
    vector = embedding['embeddings'][0]
    return vector
def completion(prompt):
    client = Client(
        host="https://ollama.com",
        headers={'Authorization': 'Bearer ' + os.getenv('OLLAMA_API_KEY')}
    )
    messages = [
    {
        'role': 'user',
        'content': prompt,
    },
    ]
    for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
        print(part['message']['content'], end='', flush=True)

    