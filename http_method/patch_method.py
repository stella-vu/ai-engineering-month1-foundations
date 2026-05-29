import requests

url = "https://api.restful-api.dev/objects/ff8081819d82fab6019e5758e9b17096"

# data = {
#     "name": "Stella's Iphone 14 Pro Max",
#     "data": {
#         "warranty": "6 months"
#     }
# }

# response = requests.patch(url, json=data)
# print(response.text)

response = requests.get(url)
object_data = response.json()

# Step 2: Modify only required fields
object_data["name"] = "Stella's Iphone 14 Pro Max"
object_data["data"]["warranty"] = "6 months"

# Step 3: Send PATCH request
response = requests.patch(url, json=object_data)

print(response.json())