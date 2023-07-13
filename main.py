from bs4 import BeautifulSoup
from requests import get
import socks
import socket

def get_ip(response):
    if response.status_code == 200:
        return response.text.replace(' ', '').rstrip()
    else:
        raise

url = 'https://api.ipify.org/?format=txt'

def check_country():
    # Realizar la solicitud GET
    try:
        response = get("https://www.cual-es-mi-ip.net/geolocalizar-ip-mapa")
    except:
        return None

    # Verificar si la solicitud fue exitosa (código de respuesta 200)
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Buscar elementos con la clase específica
        elements = soup.find_all(class_='table table-striped')

        # Imprimir los elementos encontrados
        pais = str(str(elements).split('<td>País</td>')[1].split('</strong></td>')[0].replace('<td><strong>', '').replace("\n", ""))

        return pais
    else:
        return None

quest = input('¿Quieres usar tor? [S/n]: ')
if quest == 's' or quest == 'S':
# Configuración de SOCKS proxy TOR
    ports_list = [9150, 9050]

    for ports in ports_list:
        socks.set_default_proxy(socks.SOCKS5, "localhost", ports)
        socket.socket = socks.socksocket
        try:
            response = get(url)
            break
        except Exception as e:
            pass

    # Comprobar si la solicitud fue exitosa
    try:
        if response.status_code != 200:
            print('WARNING - RECUERDA QUE HAY QUE ABRIR TOR Y CONECTARSE PARA QUE PUEDA FUNCIONAR.')
            print("ERROR - Error al hacer la solicitud HTTP GET a la página web.")
            try:
                print('ERROR - '+e)
            except:
                pass
    except NameError:
        print('WARNING - RECUERDA QUE HAY QUE ABRIR TOR Y CONECTARSE PARA QUE PUEDA FUNCIONAR.')
        print("ERROR - Error al hacer la solicitud HTTP GET a la página web.")
else:
    # Realizar la solicitud HTTP GET a la página web
    try:
        response = get(url)
    except:
        raise

print(f'{get_ip(response)} - {check_country()}')
