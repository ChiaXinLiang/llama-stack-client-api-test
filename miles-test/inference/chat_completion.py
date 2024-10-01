{
  "model": "string",
  "messages": [
    {
      "role": "user",
      "content": "string",
      "context": "string"
    },
    {
      "role": "system",
      "content": "string"
    },
    {
      "role": "ipython",
      "call_id": "string",
      "tool_name": "brave_search",
      "content": "string"
    },
    {
      "role": "assistant",
      "content": "string",
      "stop_reason": "end_of_turn",
      "tool_calls": [
        {
          "call_id": "string",
          "tool_name": "brave_search",
          "arguments": {
            "additionalProp1": "string",
            "additionalProp2": "string",
            "additionalProp3": "string"
          }
        }
      ]
    }
  ],
  "sampling_params": {
    "strategy": "greedy",
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 0,
    "max_tokens": 0,
    "repetition_penalty": 1
  },
  "tools": [
    {
      "tool_name": "brave_search",
      "description": "string",
      "parameters": {
        "additionalProp1": {
          "param_type": "string",
          "description": "string",
          "required": true,
          "default": "string"
        },
        "additionalProp2": {
          "param_type": "string",
          "description": "string",
          "required": true,
          "default": "string"
        },
        "additionalProp3": {
          "param_type": "string",
          "description": "string",
          "required": true,
          "default": "string"
        }
      }
    }
  ],
  "tool_choice": "auto",
  "tool_prompt_format": "json",
  "stream": false,
  "logprobs": {
    "top_k": 0
  }
}
