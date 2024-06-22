import requests

endpoint = "http://localhost:8000/api/classes/3/update/"

data = {
    'title': 'Beginners 2',
    'start_date': '2024-08-01',
    'description': 'For kids under 13'
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
