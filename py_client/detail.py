import requests

endpoint = "http://localhost:8000/api/classes/7/"

get_response = requests.get(endpoint)
print(get_response.json())
