from dotenv import load_dotenv
import os

load_dotenv('.env.local')

TEMPERATURE_FUNCTION = {
    "type": "function_call",
    "function_name": "get_boiling_point",
    "description": "Get the boiling point of various liquids",
    "parameters": {
        "liquid_name": {
            "param_type": "string",
            "description": "The name of the liquid",
            "required": True
        },
        "celsius": {
            "param_type": "boolean",
            "description": "Whether to return the boiling point in Celsius (True) or Fahrenheit (False)",
            "required": False,
            "default": True
        }
    },
}

MEMORY_TOOL = {
    "type": "memory",
    "memory_bank_configs": [{
        "bank_id": "18d01413-d115-4a7c-9f3d-422240b5149d",
        "type": "vector", 
        "embedding_model": "all-MiniLM-L6-v2", 
        "chunk_size_in_tokens": 2000,
        "overlap_size_in_tokens": 500
    }], 
    "query_generator_config": {
        "type": "default", 
    }, 
    "max_tokens_in_context": 4096,
    "max_chunks": 1,
}

SEARCH_TOOL = {
    "type": "brave_search",
    "api_key": os.getenv('BRAVE_API_KEY'),
    "engine": "brave",
}

CODE_INTERPRETER_TOOL = {
    "type": "code_interpreter",
    "enable_inline_code_execution": True,
}

COLOR_FUNCTION = {
    "type": "function_call",
    "function_name": "get_color",
    "description": "Get the color of various objects or substances",
    "parameters": {
        "object_name": {
            "param_type": "string",
            "description": "The name of the object or substance",
            "required": True
        },
        "format": {
            "param_type": "string",
            "description": "The format to return the color in (e.g., 'hex', 'rgb', 'name')",
            "required": False,
            "default": "name"
        }
    },
    "remote_execution": {
        "url": {"uri":"http://45.76.222.23:9999/get_color",},
        "method": "POST",
        "params": {},
        "headers": {
            "Content-Type": "application/json",
        },
        "body": {
            "object_name": "{object_name}",
            "format": "{format}"
        }
    }
}

SEARCH_FUNCTION = {
    "type": "function_call",
    "function_name": "make_web_search",
    "description": "Search the web / internet for more realtime information",
    "parameters": {
        "query": {
            "param_type": "string",
            "description": "The query to search for",
            "required": True
        }
    }
}
