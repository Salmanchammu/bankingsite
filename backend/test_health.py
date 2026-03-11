import requests
import json

def check_health():
    try:
        response = requests.get('http://127.0.0.1:5000/api/health')
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error connecting to backend: {e}")

if __name__ == "__main__":
    check_health()
