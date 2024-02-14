import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('datos/champions_2016_2022.csv', delimiter=';', encoding='latin1')

# Divide la columna SEASON en dos partes usando el guion y toma el primer elemento como el año de inicio de la temporada
df['SEASON'] = df['SEASON'].str.split('-').str[0]

# Convierte la columna SEASON a formato de fecha
df['SEASON'] = pd.to_datetime(df['SEASON'], format='%Y')

# Itera sobre las temporadas y guarda cada subconjunto en un nuevo CSV
for year in range(2016, 2022):
    # Filtra los datos para la temporada actual
    current_season = df[(df['SEASON'] >= f'{year}') & (df['SEASON'] < f'{year+1}')]
    
    # Guarda el subconjunto en un nuevo CSV
    current_season.to_csv(f'champions_{year}-{year+1}.csv', index=False, sep=',', encoding='utf-8-sig')
