import requests

headers = {'Authorization': 'Bearer 3d03079af613f3ac050b7de7ce06608ae3e1f90a'}
endpoint = "http://localhost:8000/api/classes/"

data = {
    'title': 'Girlstyle',
    'start_date': '2024-07-01'
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
