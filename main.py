from bs4 import BeautifulSoup
import requests
import socks
import socket

url = 'https://whoer.net'

quest = input('¿Quieres usar tor? [S/n]: ')
if quest == 's' or quest == 'S':
# Configuración de SOCKS proxy TOR
    ports_list = [9150, 9050]
    response = None

    for ports in ports_list:
        socks.set_default_proxy(socks.SOCKS5, "localhost", ports)
        socket.socket = socks.socksocket
        try:
            response = requests.get(url)
            break
        except Exception as e:
            pass

    # Comprobar si la solicitud fue exitosa
    if response.status_code != 200 or response == None:
        print('WARNING - RECUERDA QUE HAY QUE ABRIR TOR Y CONECTARSE PARA QUE PUEDA FUNCIONAR.')
        print("ERROR - Error al hacer la solicitud HTTP GET a la página web.")
else:
    # Realizar la solicitud HTTP GET a la página web
    import requests
    response = requests.get(url)

# Parsear el contenido HTML utilizando BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar los elementos HTML que contienen los nombres y precios de los productos
ip_find = soup.find_all('div', class_="button_icon your-ip")

# Iterar sobre los elementos encontrados e imprimir los nombres y precios de los productos
for ip_data in ip_find:         
    try:
        ip_sucio = ip_data.find('strong', class_="your-ip").text
        ip = ip_sucio.replace('\n', '')

        print(ip)
    except Exception as e:
        print(e)
