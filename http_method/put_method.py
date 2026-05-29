import requests

url = "https://api.restful-api.dev/objects/ff8081819d82fab6019e5758e9b17096"

data = {
    "name": "Iphone 14 Pro Max",
    "data": {
        "price": 1399,
        "color": "silver",
        "storage": "256GB",
        "warranty": "1 year"
    }
}

response = requests.put(url, json=data)
print(response.text)