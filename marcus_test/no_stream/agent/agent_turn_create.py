# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import requests
import os
from dotenv import load_dotenv
from typing import List
from datetime import datetime
import json
from CONSTANT.tool_lists import TEMPERATURE_FUNCTION, COLOR_FUNCTION, SEARCH_TOOL

# Load environment variables
load_dotenv('.env.local')

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

def create_agent_turn(agent_id: str, session_id: str, instruction: str, messages: List[dict]):
    url = f'http://{HOST}:{PORT}/agents/turn/create'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'X-LlamaStack-ProviderData': 'meta-reference' 

    }
    payload = {
        "agent_id": agent_id,
        "session_id": session_id,
        "instruction": instruction,
        "messages": messages,
        # "sampling_params": {
        #     "strategy": "greedy",
        #     "temperature": 0.6,
        #     "top_p": 0.95,
        #     "top_k": 40,
        #     "max_tokens": 2000,
        #     "repetition_penalty": 1.2
        # },
        # "tools": [
        #     SEARCH_TOOL,
        #     TEMPERATURE_FUNCTION,
        #     COLOR_FUNCTION
        # ],
        # "tool_choice": "auto",
        # "tool_prompt_format": "python_list", #[python_list]
        "stream": False
    }

    response = requests.post(url, headers=headers, json=payload)
    return response

def main():
    # For demonstration purposes, we'll use dummy agent_id and session_id
    agent_id = os.getenv('TEST_AGENT')
    session_id = os.getenv('TEST_SESSION')

    # Example messages
    instruction = ""

    messages = [
        # {
        #     "role": "ipython",
        #     "call_id": "eb94ff7d-858c-4eff-a938-b110bc81e3be",
        #     "tool_name": "get_color",
        #     "content": "",
        # }
        {
            "role": "user",
            "content": "continue"
        }
    ]

    # Create a turn
    turn_response = create_agent_turn(agent_id, session_id, instruction, messages)
    
    events = []
    for line in turn_response.text.splitlines():
        if line.startswith('data: '):
            json_part = line[6:]  # Remove the 'data: ' prefix
            events.append(json.loads(json_part))

    # Construct the final result
    result = {
        "agent_id": agent_id,
        "session_id": session_id,
        "turn_response": {
            "events": events
        }
    }
    
    # Convert result to JSON string and write to result.json
    json_result = json.dumps(result, indent=4)
    
    print(json_result)

if __name__ == "__main__":
    main()
