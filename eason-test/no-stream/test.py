import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv('.env.local')

def test_get_models_list():
    host = os.getenv('HOST')
    port = os.getenv('PORT')
    url = f'http://{host}:{port}/models/list'
    headers = {'accept': 'application/json'}
    
    response = requests.get(url, headers=headers)
    
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    
    data = response.json()
    assert isinstance(data, list)
    
    # You might want to add more specific assertions based on the expected response structure
    # For example:
    # assert len(data) > 0
    # assert 'model_name' in data[0]
    
    print("GET /models/list test passed successfully")
    print("Response data:", data)

if __name__ == "__main__":
    test_get_models_list()
