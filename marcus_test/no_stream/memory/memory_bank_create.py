import requests
import os
from dotenv import load_dotenv
from typing import Dict
from datetime import datetime

# Load environment variables
load_dotenv('.env.local')

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

def create_memory_bank():
    url = f'http://{HOST}:{PORT}/memory/create'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    payload = {
        "name": "testing 888",
        "config": {
            "type": "vector", 
            "embedding_model": "all-MiniLM-L6-v2", 
            "chunk_size_in_tokens": 2000, 
            "overlap_size_in_tokens": 500,
        },
        # "url": "", 
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def main():

    # Create the memory bank
    response = create_memory_bank()
    print(response)

if __name__ == "__main__":
    main()
