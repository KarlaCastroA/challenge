import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# Conexion al documento
file_key = "test.json"
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(file_key, scope)
client = gspread.authorize(creds)
sheet = client.open("test")
hoja1 = sheet.sheet1  


#extraer data
col_author = hoja1.col_values(1)
unique_author = sorted(set(col_author[1:]))

col_sentiment = hoja1.col_values(2)

col_country = hoja1.col_values(3)
unique_country = sorted(set(col_country[1:]))

col_theme = hoja1.col_values(4)
unique_theme = sorted(set(col_theme[1:]))


pivot_tuple = [] # Pivot: Author - Sentiment
for i in range(1,len(col_author)-1):
    pivot_tuple.append((col_author[i],col_sentiment[i]))


index_pivot_tuple = [] # Lista de indices por cada pivote
for tupla1 in set(pivot_tuple):
  indices = []
  for i in range(len(pivot_tuple)):
    if tupla1 == pivot_tuple[i]:
      indices.append(i)
  index_pivot_tuple.append(indices)


index_pivot_tuple = sorted(index_pivot_tuple)

# crear filas de la tabla
cabecera = [col_author[0], col_sentiment[0]] + unique_country + unique_theme
rows = [ [] for i in range(len(unique_author)) ] # matriz de valores


for i in range(len(index_pivot_tuple)):
  rows[i].append(col_author[1:][index_pivot_tuple[i][0]])
  rows[i].append(col_sentiment[1:][index_pivot_tuple[i][0]])
  
  # crete rows true/false of country and themes, set false by default
  country = [ "Falso" for i in range(len(unique_country))]
  theme = [ "Falso" for i in range(len(unique_theme)) ] 

  for index in index_pivot_tuple[i]:
    country_name = col_country[1:][index]
    index_unique_country = unique_country.index(country_name)
    country[index_unique_country] = "Verdadero"

    theme_name = col_theme[1:][index]
    index_unique_theme = unique_theme.index(theme_name)
    theme[index_unique_theme] = "Verdadero"

  rows[i] += country + theme

# escribir en la nueva hoja
new_file = "Result"
sheet.add_worksheet(title=new_file, rows=50, cols=26)
hoja2 = sheet.get_worksheet(1)   #Abrir spreadhseet

hoja2.insert_row(cabecera, index=2)

for i in range(len(rows)):
  hoja2.insert_row(rows[i], index=3+i)

