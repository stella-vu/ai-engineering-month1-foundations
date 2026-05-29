import requests

url = "https://api.restful-api.dev/objects/ff8081819d82fab6019e5758e9b17096"

response = requests.delete(url)
print(response.text)