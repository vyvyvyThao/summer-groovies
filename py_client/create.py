import requests

endpoint = "http://localhost:8000/api/classes/"

data = {
    'title': 'Girlstyle',
    'start_date': '2024-07-01'
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
