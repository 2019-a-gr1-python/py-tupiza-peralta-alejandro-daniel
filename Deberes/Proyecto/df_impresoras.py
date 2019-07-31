# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:46:32 2019

@author: ad_tp
"""

import pandas as pd
import os
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

path_impresoras = 'C:/Users/ad_tp/OneDrive/Documentos/GitHub/py-tupiza-peralta-alejandro-daniel/Deberes/Proyecto/proyecto_scrapy/scrapyP/impresoras_items.csv'

columnas_a_usar = ['titulo','modelo','marca',
                  'precio','condicion','opiniones',
                   'tipo_vendedor','ventas_vendedor']

df_impresoras = pd.read_csv(
        path_impresoras,
        usecols=columnas_a_usar,
        index_col='titulo'
        )

pv_primeros_cinco= df_impresoras2.filter(items = ["titulo","ventas_vendedor"]).sort_values('ventas_vendedor', ascending=False).head(5)



precio = df_impresoras.filter(items = ["modelo","precio"]).sort_values('precio', ascending=False)


import matplotlib.pyplot as plt
from pandas.tools.plotting import table

df_impresoras2 = pd.read_csv(
        path_impresoras,
        usecols=columnas_a_usar,
        )

precio2 = df_impresoras2.filter(items = ["titulo","precio"]).sort_values('precio', ascending=False)

precio3 = df_impresoras2.filter(items = ["titulo","ventas_vendedor"]).sort_values('ventas_vendedor', ascending=False)



df = pd.DataFrame(precio2, columns = ['titulo','ventas_vendedor'])


opiniones = np.unique(df_impresoras2['opiniones'].get_values(), return_counts = True)
title = pd.Series(opiniones[1],
                          index=opiniones[0]
                         )

opi = title.sort_values(ascending=False).index.values.tolist()
pio = title.sort_values(ascending=False)
posicion_y = np.arange(len(opi))
plt.figure(figsize=(10,15))
plt.barh(posicion_y, pio, align = "center")
plt.yticks(posicion_y, opi)
plt.xlabel('Ocurrencia', fontsize=10)
plt.title("Cantidad de crímenes por Barrio", fontsize=10)
for i, v in enumerate(pio):
    plt.text(v + 3, i, str(v),fontsize='large')
plt.show()

cols = ['precio']
df[cols] = df[cols].applymap(lambda x: '{0:.4f}'.format(x))
print (df)


titulos = np.unique(df_impresoras2['titulo'].get_values(), return_counts = True)[0]
precios = df_impresoras2['precio'].get_values()

posicion_y = np.arange(len(precios))
plt.figure(figsize=(5,15))
plt.barh(posicion_y, precios, align = "center")
plt.yticks(posicion_y, titulos)
plt.xlabel('Aproximado', fontsize=10)
plt.title("Cantidad de valoracion por producto", fontsize=15)
for i, v in enumerate(precios):
    plt.text(v + 3, i, str(v),fontsize='x-large')
plt.show()





precio2['Precios'] = df['precio']
plt.figure(figsize=(16,8))
# plot chart
ax1 = plt.subplot(121, aspect='equal')

pv_primeros_cinco.plot(kind='pie', y = 'ventas_vendedor', ax=ax1, autopct='%1.1f%%', 
 startangle=90, shadow=False, labels=df['titulo'], legend = False, fontsize=14)
plt.axis('equal')

# View the plot
plt.show()

# plot table
ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, pv_primeros_cinco, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(14)
plt.show()
