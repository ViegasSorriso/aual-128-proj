from bs4 import BeautifulSoup as bs
import pandas as pd
import requests


START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Faça uma requisição da página usando o módulo request, descomente para funcionar
site = requests.get(START_URL)
print("site:", site)

soup = bs(site.text, "html.parser")

# Obtenha todas as tabelas da página usando o método find_all()
# Obtenha a <table> com classe = 'wikitable sortable', descomente o correto
star_table = soup.find_all('table', {"class": "wikitable sortable"})


total_table = len(star_table)

# Crie uma lista vazia, descomente o correto
temp_list = []

# OBSERVAÇÃO IMPORTANTE: A página na URL fornecida é mantida pela "wikipedia" e pode ser atualizada no futuro.
# Portanto, verifique o número de índice apropriado de star_table[1]
# Atualmente há 3 tabelas com classe = "class":"wikitable sortable" e a tabela "Field brown dwarfs" é a segunda tabela
# Portanto, o índice é 1
table_rows = star_table[1].find_all('tr')

# Loop for para extrair todas as tags <td>
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance = []
Mass = []
Radius = []

print("temp_list:", temp_list)

for i in range(1, len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

headers = ['Star_name', 'Distance', 'Mass', 'Radius']

# Defina o dataframe do Pandas
df2 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius,)),
                   columns=['Star_name', 'Distance', 'Mass', 'Radius'])
print("df2:", df2)

# Converta para CSV
df2.to_csv('dwarf_stars.csv', index=True, index_label="id")
