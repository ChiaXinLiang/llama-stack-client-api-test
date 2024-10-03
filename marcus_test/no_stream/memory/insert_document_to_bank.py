import requests
import os
from dotenv import load_dotenv
from typing import Dict
from datetime import datetime
from CONSTANT.document_list import MEMORY_BANK_DOCUMENT, URL_DOCUMENT

# Load environment variables
load_dotenv('.env.local')

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

def insert_document_to_bank():
    url = f'http://{HOST}:{PORT}/memory/insert'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    payload = {
        "bank_id": "18d01413-d115-4a7c-9f3d-422240b5149d",
        "document": [
            # MEMORY_BANK_DOCUMENT,
            URL_DOCUMENT
        ],
        "ttl_seconds": 0,
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def main():
    # Example usage
    response = insert_document_to_bank()
    print(response)

if __name__ == "__main__":
    main()
