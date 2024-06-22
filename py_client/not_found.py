import requests

endpoint = "http://localhost:8000/api/classes/12908309812/"

get_response = requests.get(endpoint)
print(get_response.json())