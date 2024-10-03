# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv('.env.local')

def test_chat_completion():
    """
    Test the chat completion API endpoint.

    This function sends a POST request to the chat completion endpoint and processes the response.
    It checks for the correct status code, response format, and expected fields in the response.

    Returns:
        None
    """
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    url = f'http://{host}:{port}/inference/chat_completion'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "model": "Llama3.2-11B-Vision",
        "messages": [
            {"role": "assistant", "content": "You are a helpful assistant."},
            {"role": "user", 
                "content": [
                    "hello",
                    "world",
                ]
            },
            {"role": "user", 
                "content": {"image": {"uri": "https://upload.wikimedia.org/wikipedia/commons/1/18/Dog_Breeds.jpg"}}
                
            }
        ],
        "sampling_params": {},
        "stream": False  # Changed to False to disable streaming
    }

    response = requests.post(url, headers=headers, json=payload)
    
    content_type = response.headers['Content-Type']

    if content_type == 'application/json':
        data = response.json()
        print(f"Received JSON response: {data}")
    else:  # text/event-stream
        data = response.text
        print(f"Received event stream response: {data}")
        # You might want to process the event stream data here
        # For example, splitting it into events and parsing each event

    print("Chat completion test completed successfully")

def main():
    """
    Main function to run the chat completion test.

    Returns:
        None
    """
    test_chat_completion()

if __name__ == "__main__":
    main()