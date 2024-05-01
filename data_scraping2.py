from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd 
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'

page=requests.get(bright_stars_url)
soup=bs(page.text,'html.parser')
star_table=soup.find('table')
temp_list=[]
table_rows=star_table.find_all('tr')
for tr in table_rows:
    td =tr.find_all('td')

star_names=[]
dist=[]
mass=[]
radius=[]


df2=pd.DataFrame(list(zip(star_names,dist,mass,radius)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)
df2.to_csv('dwarf_stars.csv')