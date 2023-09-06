import requests
from bs4 import BeautifulSoup

url = "https://www.ambito.com/contenidos/dolar.html"
headers = {
    "User-Agent": "Tu Agente de Usuario",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Ahora puedes buscar y extraer la información que necesitas de la página web.
    # Por ejemplo, puedes encontrar elementos por etiquetas, clases o IDs.

    # Ejemplo:
    cotizacion_dolar = soup.find("span", class_="variation-max-min__value data-valor data-venta").text
    print(f"Cotización del Dólar: {cotizacion_dolar}")
else:
    print(f"No se pudo acceder a la página. Código de estado: {response.status_code}")
