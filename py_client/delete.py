import requests
from getpass import getpass

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Enter username: ")
password = getpass('Enter password: ')

auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f'Bearer {token}'
    }

    class_id = input("What is the product id you want to use?\n")

    try: 
        class_id = int(class_id)
    except:
        class_id = None
        print(f"{class_id} is not a valid id")

    if class_id:
        endpoint = f"http://localhost:8000/api/classes/{class_id}/delete/"

get_response = requests.delete(endpoint, headers=headers)
print(get_response.status_code, get_response.status_code==204)