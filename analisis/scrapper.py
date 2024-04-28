from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep
import csv

# Configuración inicial de Selenium y ChromeDriver
chrome_driver_path =  "C:/Users/alvde/Desktop/chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL del equipo de PSG en FootyStats
url = "https://footystats.org/clubs/paris-saint-germain-fc-68"

# Iniciar el driver y navegar a la página
driver.get(url)
sleep(3)  # Pausa para asegurar que la página se carga completamente

# Abrir archivo CSV para escribir los datos
with open('psg_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Categoria', 'Datos'])  # Escribir la cabecera del archivo CSV

    # Estadísticas generales del equipo
    general_stats = driver.find_element(By.CSS_SELECTOR, "div.general-stats").text
    writer.writerow(['Estadísticas generales del equipo', general_stats])

    # Información de jugadores
    players_info = driver.find_elements(By.CSS_SELECTOR, "table#squad-table tbody tr")
    for player in players_info:
        writer.writerow(['Jugador', player.text])

    # Resultados de partidos recientes
    recent_matches = driver.find_elements(By.CSS_SELECTOR, "div.recent-matches div.match")
    for match in recent_matches:
        writer.writerow(['Partido reciente', match.text])

    # Clasificación en la liga
    league_position = driver.find_element(By.CSS_SELECTOR, "div.league-position").text
    writer.writerow(['Clasificación en la liga', league_position])

    # Información de Champions League
    champions_info = driver.find_elements(By.CSS_SELECTOR, "div.champions-league div.match")
    for match in champions_info:
        writer.writerow(['Partido de Champions', match.text])

# Cerrar el driver después de la sesión
driver.quit()
