from ollama import Client
import os
from dotenv import load_dotenv
load_dotenv()

ollama_client = Client(
        host="https://ollama.com",
        headers={'Authorization': 'Bearer ' + os.getenv('OLLAMA_API_KEY')}
    )