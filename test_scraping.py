import requests
from bs4 import BeautifulSoup

#------------------------------

url = 'https://www.cronista.com/MercadosOnline/dolar.html'
response = requests.get(url)

#-----------------------------

soup = BeautifulSoup(response.text, 'html.parser')

# Busca todos los elementos <div> con la clase "buy-value"
buy_elements = soup.find_all('div', class_='buy-value')

# Busca todos los elementos <div> con la clase "sell-value"
sell_elements = soup.find_all('div', class_='sell-value')

# Crea un diccionario para almacenar los valores
dolar_info = {'Dolar BNA': {},'Dolar Blue': {},'Dolar MEP': {}}

# Verifica si se encontraron elementos en la búsqueda de "buy-value"
if buy_elements:
    # El primer elemento de la lista de "buy-value" es el valor de "Compra"
    dolar_info['Dolar BNA']['Compra'] = buy_elements[0].text.strip()
    dolar_info['Dolar Blue']['Compra'] = buy_elements[1].text.strip()
    dolar_info['Dolar MEP']['Compra'] = buy_elements[4].text.strip()

# Verifica si se encontraron elementos en la búsqueda de "sell-value"
if sell_elements:
    # El primer elemento de la lista de "sell-value" es el valor de "Venta"
    dolar_info['Dolar BNA']['Venta'] = sell_elements[0].text.strip()
    dolar_info['Dolar Blue']['Venta'] = sell_elements[1].text.strip()
    dolar_info['Dolar MEP']['Venta'] = sell_elements[5].text.strip()

# Imprime el diccionario
print(dolar_info)
