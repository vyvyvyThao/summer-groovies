import requests

class_id = input("What is the product id you want to use?\n")

try: 
    class_id = int(class_id)
except:
    class_id = None
    print(f"{class_id} is not a valid id")

if class_id:
    endpoint = f"http://localhost:8000/api/classes/{class_id}/delete/"

get_response = requests.delete(endpoint)
print(get_response.status_code, get_response.status_code==204)