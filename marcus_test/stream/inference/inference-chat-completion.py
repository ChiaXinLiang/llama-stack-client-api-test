# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import aiohttp
import asyncio
import os
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import base64
import wget


# Load environment variables from .env.local
load_dotenv('.env.local')

# Download the image
local_image_path = "dog_breeds.jpg"
# Open the local image
image = Image.open(local_image_path)
buffered = BytesIO()
image.save(buffered, format="PNG")
img_str = f"data:image/png;base64,{base64.b64encode(buffered.getvalue()).decode()}"
print(img_str)

async def test_chat_completion():
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
            {"role": "system", "content": "You are Allen."},
            {"role": "user", "content": ["hello, Allen, the following is a image",
                                        #  {"image": {"uri": "https://upload.wikimedia.org/wikipedia/commons/1/18/Dog_Breeds.jpg"}},
                                        {"image" : img_str},
                                         "What is this image talks about?"]},
        ],
        "sampling_params": {},
        "stream": True  # Changed to True to enable streaming
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=payload) as response:
            assert response.status == 200, f"Unexpected status code: {response.status}"
            assert response.headers['Content-Type'] == 'text/event-stream; charset=utf-8', f"Unexpected content type: {response.headers['Content-Type']}"
            
            async for line in response.content:
                event = line.decode('utf-8').strip()
                if event:
                    print(f"Received event: {event}")

            print("Chat completion test completed successfully")

async def main():
    """
    Main function to run the chat completion test.

    Returns:
        None
    """
    await test_chat_completion()

if __name__ == "__main__":
    asyncio.run(main())