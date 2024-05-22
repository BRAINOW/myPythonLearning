import requests

response = requests.get("https://api.github.com")
#print(response) # <Response [200]> 
#print(response.headers)
#print(response.status_code) #200

#Formmas de ver los datos 
#print(response.content) #Retorna la respuesta en bytes
#print(response.text) #Respuesta en forma de texto
#print(response.json()) #Convierte el cuerpo de la respuesta en un diccionario
print(response.json()["current_user_url"])
