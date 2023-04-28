

import requests

#GET
headers = {'accept': 'application/json'}
status ='available'

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers=headers)

print(res.status_code)


#POST
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
data = {"id": 9456118654, "category": {"id": 0, "name": "string"}, "name": "Lilo", "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "Lilo"}], "status": "available"}

res1 = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=data)

print(res1.status_code)
print(res1.json())


#PUT
headers = {'accept': 'application/json',
           'Content-Type': 'application/json'}
data = {"id": 9456118654, "category": {"id": 0, "name": "string"}, "name": "Roki", "photoUrls": ["string"],
       "tags": [{"id": 0, "name": "Lilo"}], "status": "available"}


res2 = requests.put(f"https://petstore.swagger.io/v2/pet", headers=headers, json=data)
print(res2.status_code)
print(res2.json())

#DELETE
headers = {'accept': 'application/json'}
petId = 9456118654

res3 = requests.delete(f"https://petstore.swagger.io/v2/pet/{petId}", headers=headers)

print(res3.status_code)
print(res3.json())

res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers=headers)

print(res.status_code)
