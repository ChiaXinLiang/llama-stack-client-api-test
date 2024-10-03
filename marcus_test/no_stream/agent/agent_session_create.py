# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import requests
import os
from dotenv import load_dotenv
from datetime import datetime
from CONSTANT.memory_bank_list import VECTOR_MEMORY_BANK

# Load environment variables
load_dotenv('.env.local')

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

def create_agent_session(agent_id: str):
    url = f'http://{HOST}:{PORT}/agents/session/create'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }
    payload = {
        "agent_id": agent_id,
        "session_name": "chat bot",
        "started_at": datetime.now().isoformat(), 
        # "memory_bank": VECTOR_MEMORY_BANK
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def main():
    # For demonstration purposes, we'll use a dummy agent_id
    agent_id = os.getenv('TEST_AGENT')

    # Create a session
    session_response = create_agent_session(agent_id)
    session_id = session_response['session_id']
    print(f"Session created with ID: {session_id}")

if __name__ == "__main__":
    main()
