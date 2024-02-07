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

        #Encontar la tabla de resultados (inspeccionar pero ahora pruebo)
        tabla = soup.find('div', {'class': 'sc-jlZhew kgghii'})

        #lista para almacenar datos
        partidos = []

        #iteramos sobre las filas de la tabla
        for fila in tabla.find_all('div', {'class': 'sc-fqkvVR byYarT'}):
            #extraer los datos
            local_team= fila.find('div', {'class': 'sc-fqkvVR byYarT'}).text.strip()


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
           