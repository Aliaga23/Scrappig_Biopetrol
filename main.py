import requests
from bs4 import BeautifulSoup

url = "http://ec2-3-22-240-207.us-east-2.compute.amazonaws.com/guiasaldos/main/donde/134"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tarjetas = soup.find_all("div", class_="btn-bio-app")

datos_estaciones = []

for tarjeta in tarjetas:
    bloques = tarjeta.find_all("div", class_="col-12")

    nombre = bloques[0].text.strip()
    litros = bloques[2].text.strip()
    fecha = bloques[4].text.strip()
    direccion = tarjeta.find("div", class_="alert-secondary").text.strip().split("\n")[0]

    datos_estaciones.append({
        "nombre": nombre,
        "litros": litros,
        "fecha": fecha,
        "direccion": direccion
    })

for est in datos_estaciones:
    print(est)
