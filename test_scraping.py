import requests
from bs4 import BeautifulSoup
import json

def dolarArg():
    # URL de la página web
    url = 'https://www.cronista.com/MercadosOnline/dolar.html'
    
    try:
        # Realizar la solicitud GET
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción si la solicitud falla

        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar los elementos de compra y venta
        buy_elements = soup.find_all('div', class_='buy-value')
        sell_elements = soup.find_all('div', class_='sell-value')

        # Crear un diccionario para almacenar los valores
        dolar_info = {'Dolar BNA': {}, 'Dolar Blue': {}, 'Dolar MEP': {}}

        # Extraer los valores de compra si están disponibles
        if buy_elements:
            dolar_info['Dolar BNA']['Compra'] = buy_elements[0].text.strip()
            dolar_info['Dolar Blue']['Compra'] = buy_elements[1].text.strip()
            dolar_info['Dolar MEP']['Compra'] = buy_elements[4].text.strip()

        # Extraer los valores de venta si están disponibles
        if sell_elements:
            dolar_info['Dolar BNA']['Venta'] = sell_elements[0].text.strip()
            dolar_info['Dolar Blue']['Venta'] = sell_elements[1].text.strip()
            dolar_info['Dolar MEP']['Venta'] = sell_elements[5].text.strip()

        # Convertir el diccionario en una cadena JSON y devolverla
        json_data = json.dumps(dolar_info, indent=4)
        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la información: {e}")
        return None
    

def dolarVzla():
    # URL de la página web
    url = 'https://dollar-frontend-api.vercel.app/'
    
    try:
        # Realizar la solicitud GET
        response = requests.get(url)
        response.raise_for_status()  # Lanzar una excepción si la solicitud falla

        # Crear un objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar todas las etiquetas <h2> con class="dolar-origin" y texto específico
        h2_elements = soup.find_all('h2', class_='dolar-origin', text=['BCV', 'Monitor Dolar Venezuela', 'Monitor Dolar Vzla'])

        # Crear un diccionario para almacenar las etiquetas <h2> y sus respectivas etiquetas <h3>
        dolar_info = {}

        # Extraer los elementos <h3> dentro de los elementos <h2> encontrados
        for h2_element in h2_elements:
            h3_elements = h2_element.find_next('h3')
            h3_text = h3_elements.text.strip()
            dolar_info[h2_element.text.strip()] = h3_text

        # Convertir el diccionario en una cadena JSON y devolverla
        json_data = json.dumps(dolar_info, indent=4)
        return json_data

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la información: {e}")
        return None

# Ejemplo de uso de la función
if __name__ == "__main__":
    json_info = dolarVzla()
    if json_info:
        print(json_info)
