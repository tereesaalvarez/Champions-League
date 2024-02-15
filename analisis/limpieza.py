import pandas as pd

# Lee el archivo CSV
#df_2016_2022 = pd.read_csv('datos/champions_2016_2022_mal.csv', delimiter=';', encoding='latin1')
#df_2022_2023 = pd.read_csv('datos/champions_2022_2023_mal.csv', delimiter=';', encoding='latin1')

# conservar las columnas que quiero usar de cada dataset
#df_2016_2022_bien = df_2016_2022[['SEASON', 'HOME_TEAM', 'AWAY_TEAM', 'HT_SCORE', 'AW_SCORE']]
#df_2022_2023_bien = df_2022_2023[['SEASON', 'HOME_TEAM', 'AWAY_TEAM', 'HT_SCORE', 'AW_SCORE']]

# guardar dataframes limpios en nuevos archivos csv
#df_2016_2022_bien.to_csv('datos/champions_2016_2022.csv', index=False, sep=',', encoding='utf-8-sig')
#df_2022_2023_bien.to_csv('datos/champions_2022_2023.csv', index=False, sep=',', encoding='utf-8-sig')

df = pd.read_csv('datos_limpios/champions_2022_2023.csv')

#Diccionario de cambio de nombres para que coincidan con los otros csv
cambios_nombre = {
    'Milan': 'AC Milan',
    'Club Brugge': 'Club Brugge KV',
    'PSG': 'Paris Saint-Germain',
    'AtlÃ©tico de Madrid': 'Atlético Madrid',
    'Liverpool': 'Liverpool FC',
    'Ajax': 'AFC Ajax',
    'Barcelona': 'FC Barcelona',
    'Bayern Munich': 'Bayern München',
    'Benfica': 'SL Benfica',
    'Sevilla': 'Sevilla FC',
    'Chelsea': 'Chelsea FC',
    'Napoli': 'SSC Napoli',
    'FC Copenhagen': 'FC København',
    'Celtic': 'Celtic FC',
    'Viktoria PlzeÅ': 'Viktoria Plze?',
    'Marseille': 'Olympique Marseille'
}

# Realiza los cambios de nombres en las columnas HOME_TEAM y AWAY_TEAM
df['HOME_TEAM'].replace(cambios_nombre, inplace=True)
df['AWAY_TEAM'].replace(cambios_nombre, inplace=True)

# guardar el dataframe modificado en la carpeta datos_limpios
df.to_csv('datos_limpios/champions_2022_2023.csv', index=False, sep=',', encoding='utf-8-sig')