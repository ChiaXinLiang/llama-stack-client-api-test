# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

import os
from dotenv import load_dotenv
import json
from agent_client import create_agent
from agent_session_create import create_agent_session
from agent_turn_create import create_agent_turn
from CONSTANT.tool_lists import TEMPERATURE_FUNCTION, SEARCH_TOOL, COLOR_FUNCTION, SEARCH_FUNCTION 
from CONSTANT.memory_bank_list import VECTOR_MEMORY_BANK

# Load environment variables
load_dotenv('.env.local')

def process_turn_response(turn_response):
    events = []
    for line in turn_response.text.splitlines():
        if line.startswith('data: '):
            json_part = line[6:]  # Remove the 'data: ' prefix
            events.append(json.loads(json_part))
    return events

def create_agent_config():
    return {
        "model": "Llama3.1-8B-Instruct",
        "instructions": "You are an an expert assistant, plaease answer me refer to the tool_lists first, use brave search or other tools to comfirm answer before reply me. <remember>use code interpreter only necessary!</remember>",        
        "enable_session_persistence": False,
        "sampling_params": {
            "strategy": "greedy",
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 10,
            "max_tokens": 2000,
            "repetition_penalty": 0.5
        },
        "tools": [
            SEARCH_TOOL,
            TEMPERATURE_FUNCTION,
            COLOR_FUNCTION
        ],
        "tool_choice": "auto",
        "tool_prompt_format": "json", #[python_list]
        "max_infer_iters": 10,
        "stream": True,
    }

def main():
    # Create an agent with specific configuration
    agent_config = create_agent_config()
    agent_response = create_agent(agent_config)
    print(agent_response)
    agent_id = agent_response.get('agent_id')
    if not agent_id:
        print("Error: Failed to create agent. No agent_id received.")
        return
    print(f"Agent created with ID: {agent_id}")

    # Create a session
    session_response = create_agent_session(agent_id)
    session_id = session_response['session_id']
    print(f"Session created with ID: {session_id}")

    # First turn: Ask about gemstones
    instruction = "Plan me step by step. "
    messages = [
        {
            "role": "user",
            # "content": """Tell me the history of taiwan?""",
            # "content": """What is the boiling point of mercury?""",
            # "content": """Tell me the color of cloud?""",
        }
    ]

    turn_response = create_agent_turn(agent_id, session_id, instruction, messages)
    events = process_turn_response(turn_response)


    # Second turn: Use the output of the first turn as input

    # Process and print the final result
    result = {
        "agent_id": agent_id,
        "session_id": session_id,
        "conversation": events
    }
    
    json_result = json.dumps(result, indent=4)
    
    if not events:
        print("Empty conversation")
    else:
        with open('result.json', 'w') as f:
            json.dump(result, f, indent=4)
        print("Conversation saved to result.json")

if __name__ == "__main__":
    main()
