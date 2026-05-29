import requests

url = "https://api.restful-api.dev/objects"

data = {
    "name": "Iphone 14 Pro Max",
    "data": {
        "price": 1599,
        "color": "silver",
        "storage": "256GB"
    }
}

response = requests.post(url, json=data)
print(response.text)