# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 01:11:52 2019

@author: ad_tp
"""

import pandas as pd
import re

scrapy view https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=447&s=0&pp=25
scrapy shell https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=447&s=0&pp=25
----------
scrapy shell 
fetch("https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=447&s=0&pp=25") 
----------
precios=response.xpath('//div[contains(@class,"price-member")]/div[@data-bind]').extract()
precios
productos = response.xpath('/html/body/div/div/div/div/div/ul/li/@data-name').extract()
productos

#Formateo de los precios
for i in range(len(precios)):
    precios[i] = re.findall(r"\d\d.\d.|\d.\d.", precios[i])

#Creación de el DataFrame
df_precios = pd.DataFrame(precios,columns=['Precios'],index=productos)
df_precios

#Transforamción del valor de string a float
df_precios['Precios'] = df_precios['Precios'].astype('float64')

#maximo
df_maximo = df_precios.values.max()
print(df_precios.loc[df_precios['Precio Total'] == df_precios['Precio Total'].max()])

#minimo
df_minimo = df_precios.values.min()
print(df_precios.loc[df_precios['Precio Total'] == df_precios['Precio Total'].min()])
