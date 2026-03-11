import requests
import json
import random

def test_signup():
    url = "http://127.0.0.1:5000/api/auth/signup"
    username = f"testuser_{random.randint(1000, 9999)}"
    payload = {
        "username": username,
        "email": f"{username}@example.com",
        "password": "password123",
        "name": "Test User",
        "device_type": "desktop"
    }
    try:
        response = requests.post(url, json=payload)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.ok
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    test_signup()
