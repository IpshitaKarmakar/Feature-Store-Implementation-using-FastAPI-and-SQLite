import requests

BASE_URL = "http://127.0.0.1:8000"

data = [
    {"entity_id": "user_1", "value": 10},
    {"entity_id": "user_1", "value": 20},
    {"entity_id": "user_1", "value": 30}
]

for item in data:
    requests.post(BASE_URL + "/register_raw", json=item)

requests.post(BASE_URL + "/compute_features/user_1")

response = requests.get(BASE_URL + "/get_features/user_1")
print(response.json())
