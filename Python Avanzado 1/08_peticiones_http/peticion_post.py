import requests

url = "https://webhook.site/e426061d-3a7a-492f-8318-c61335a7795a"

#Simularemos que es un restaurante

payload = { "plato":"pasta", "cantidad": 2 }
query_params = {"nombre":"Brian"}
response = requests.post(url, data=payload, params=query_params)
print(response.status_code) #200
print(response.text) #No tiene texto