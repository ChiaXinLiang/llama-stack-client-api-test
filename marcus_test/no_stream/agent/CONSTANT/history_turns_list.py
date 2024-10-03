HISTORY_TURN = [
    {
        "turn_id": "old_turn_id",
        "session_id": "old_session_id",
        "input_messages": [
            {
                "role": "user",
                "content": "What's the weather like today?"
            },
            {
                "role": "assist",
                "content": "The current temperature is 72°F.",
            }
        ],
        "steps": [
            {
                "model_config": "model_config",
                "step_type": "inference",
                "model_response": {
                    "role": "user",
                    "content":[],
                    "stop_reason": "",
                    "tool_calls": [
                        {
                            "call_id": "",
                            "tool_name": "",
                            "arguments": {},
                        }
                    ]
                }
            },
            {
                "step_type": "tool_execution",
                "tool_calls": {
                    "call_id": "",
                    "tool_name": "",
                    "arguments": "",
                },
                "tool_responses": [
                    {
                        "call_id": "",
                        "tool_name": "", 
                        "content": []
                    }
                ]
            },
            {
                "step_type": "memory_retrieval",
                "memory_bank_ids": [
                    "id1", "id2"
                ],
                "inserted_context": [
                    "hello, world",
                    "how are you"
                ]
            }
        ],
        "output_message": {
            "role": "assistant",
            "content": "The weather today is pleasant. The current temperature is 72°F."
        },
        "output_attachments": [],
        "started_at": "2023-06-15T10:30:00Z",
        "completed_at": "2023-06-15T10:30:05Z"
    }
]
