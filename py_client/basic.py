import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, json={'title': 'Girlstyle', 'start_date': '2024-07-01'})

# print(get_response.text)
print(get_response.json())
# print(get_response.status_code)