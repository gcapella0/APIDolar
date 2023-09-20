import requests
from bs4 import BeautifulSoup

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

        # Devolver el diccionario con la información
        return dolar_info

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la información: {e}")
        return None

# Ejemplo de uso de la función
if __name__ == "__main__":
    info_dolar = dolarArg()
    if info_dolar:
        print(info_dolar)
