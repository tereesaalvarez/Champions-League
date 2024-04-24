from selenium import webdriver
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()
driver.get("https://footystats.org/clubs/paris-saint-germain-fc-68")

# Extraer información de menús de ligas
ligas = driver.find_elements(By.CSS_SELECTOR, "div.dropDownMenu a")
with open('ligas.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Liga', 'URL'])
    for liga in ligas:
        writer.writerow([liga.text, liga.get_attribute('href')])

# Extraer información de jugadores
jugadores = driver.find_elements(By.CSS_SELECTOR, "table#squad-table tbody tr")
with open('jugadores.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre', 'Posición', 'Goles', 'Asistencias'])  # Ajustar según las columnas disponibles
    for jugador in jugadores:
        detalles = [dato.text for dato in jugador.find_elements(By.CSS_SELECTOR, 'td')]
        writer.writerow(detalles)

# Extraer resultados de partidos
resultados = driver.find_elements(By.CSS_SELECTOR, "div.match-results div.match")
with open('resultados_partidos.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Fecha', 'Local', 'Visitante', 'Resultado'])
    for resultado in resultados:
        datos = resultado.text.split('\n')
        writer.writerow(datos)

# Extraer clasificación en la liga
clasificacion = driver.find_elements(By.CSS_SELECTOR, "div.league-standings tbody tr")
with open('clasificacion_liga.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Equipo', 'PJ', 'G', 'E', 'P', 'GF', 'GC', 'DG', 'Pts'])  # Ajustar según las columnas disponibles
    for equipo in clasificacion:
        stats = [dato.text for dato in equipo.find_elements(By.CSS_SELECTOR, 'td')]
        writer.writerow(stats)

driver.quit()
