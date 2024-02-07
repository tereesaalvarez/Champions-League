import requests
from bs4 import BeautifulSoup
import csv

def champions_league_scraper(temporada):
    #url de la pagina de la champions de sofascore
    url = 'https://www.sofascore.com/es/torneo/futbol/europe/uefa-champions-league/7#id:17351,tab:matches'

    #hacemos la peticion a la pagina
    response = requests.get(url)

    #verificar si solicitud exitosa (200)
    if response.status_code == 200:
        #parseamos el contenido de la pagina
        soup = BeautifulSoup(response.text, 'html.parser')

        #Encontar la tabla de resultados
        tabla = soup.find('table', {'class': 'js-event-list-tournament-page'})

        #lista para almacenar datos
        partidos = []

        #iteramos sobre las filas de la tabla
        for fila in tabla.find_all('tr'):
            #iteramos sobre las columnas de la fila
            cols = fila.find_all('td')

            #verificar si la fila tiene datos
            if len(cols) > 0:
                #obtener datos de la fila
                fecha = cols[0].text.strip()
                local = cols[1].text.strip()
                visitante = cols[3].text.strip()
                resultado = cols[2].text.strip()
                #agregar datos a la lista
                partidos.append([fecha, local, resultado, visitante])

        #guardar datos en un archivo csv
        nombre_csv = 'champions_league_' + temporada + '.csv'
        with open(nombre_csv, 'w', newline='', encoding = 'utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Fecha', 'Local', 'Resultado', 'Visitante'])
            writer.writerows(partidos)
        
        print("Se han guardado los datos del campeonato de Europa en el archivo " + nombre_csv)
    else:
        print("Error al cargar la pagina. Codigo de estado: " + response.status_code)

#Ejecutar la funcion con una temporada especifica
champions_league_scraper('2020-2021')
           