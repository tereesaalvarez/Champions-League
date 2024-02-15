import pandas as pd

# Lee el archivo CSV
df_2016_2022 = pd.read_csv('datos/champions_2016_2022_mal.csv', delimiter=';', encoding='latin1')
df_2022_2023 = pd.read_csv('datos/champions_2022_2023_mal.csv', delimiter=';', encoding='latin1')

# conservar las columnas que quiero usar de cada dataset
df_2016_2022_bien = df_2016_2022[['SEASON', 'HOME_TEAM', 'AWAY_TEAM', 'HT_SCORE', 'AW_SCORE']]
df_2022_2023_bien = df_2022_2023[['SEASON', 'HOME_TEAM', 'AWAY_TEAM', 'HT_SCORE', 'AW_SCORE']]

# guardar dataframes limpios en nuevos archivos csv
df_2016_2022_bien.to_csv('datos/champions_2016_2022.csv', index=False, sep=',', encoding='utf-8-sig')
df_2022_2023_bien.to_csv('datos/champions_2022_2023.csv', index=False, sep=',', encoding='utf-8-sig')