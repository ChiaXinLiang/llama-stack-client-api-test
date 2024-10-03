# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import requests
import os
from dotenv import load_dotenv
from CONSTANT.tool_lists import TEMPERATURE_FUNCTION, SEARCH_TOOL, CODE_INTERPRETER_TOOL, COLOR_FUNCTION

# Load environment variables
load_dotenv('.env.local')

HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

def create_agent(agent_config):
    url = f'http://{HOST}:{PORT}/agents/create'
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    payload = {
        "agent_config": agent_config
    }

    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def main():
    # Example agent configuration
    example_agent_config = {
        "model": "Llama3.2-1B-Instruct",
        "instructions": "Your instructions here",
        "enable_session_persistence": False,
        "sampling_params": {
            "strategy": "greedy",
            "temperature": 0.7,
            "top_p": 0.9,
            "top_k": 50,
            "max_tokens": 1000,
            "repetition_penalty": 1.1
        },
        "tools": [
            SEARCH_TOOL,
            TEMPERATURE_FUNCTION,
            CODE_INTERPRETER_TOOL,
        ],
        "tool_choice": "auto",
        "tool_prompt_format": "python_list",
        "max_infer_iters": 100,
        "stream": True
    }

    # Create an agent with the example configuration
    agent_response = create_agent(example_agent_config)
    print(agent_response['agent_id'])

if __name__ == "__main__":
    main()
