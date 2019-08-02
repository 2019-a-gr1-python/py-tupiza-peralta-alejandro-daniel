# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 01:47:58 2019

@author: ad_tp
"""

import pandas as pd
import os
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

path_aparatos = 'C:/Users/ad_tp/OneDrive/Documentos/GitHub/py-tupiza-peralta-alejandro-daniel/Deberes/Proyecto/proyecto_scrapy/proyecto/computadoras_items.csv'

columnas_para_usar = ['titulo','modelo','marca',
                  'precio','condicion','opiniones',
                   'tipo_vendedor','ventas_vendedor']

df_aparatos = pd.read_csv(
        path_aparatos,
        usecols=columnas_para_usar,
        )

df_c = pd.read_csv(
        path_aparatos,
        usecols=columnas_para_usar,
        index_col='titulo'
        )

filtrado = df_aparatos.filter(items = ["titulo","ventas_vendedor"]).sort_values('ventas_vendedor', ascending=False)

datos_a = df_c.filter(items = ["titulo","ventas_vendedor"]).sort_values('ventas_vendedor', ascending=False)

seccion_df = filtrado.iloc[18:25,:].copy()

seccion_amplia = filtrado.iloc[5:35,:].copy()

pv_a = filtrado.filter(items = ["titulo","ventas_vendedor"]).sort_values('ventas_vendedor', ascending=False)
datos = pv_a
datos.plot(kind="bar",title="Ventas por id de productos vendidos")

pv_tabla2 = datos_a.filter(items = ["titulo","ventas_vendedor"]).sort_values('ventas_vendedor', ascending=False).tail(12)

ax2 = plt.subplot(122)
plt.axis('off')
tbl = table(ax2, pv_tabla2, loc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(11)
plt.show()

filtro_marcas = df_aparatos.filter(items = ["titulo","marca"]).sort_values('marca', ascending=False)
sec_marca = filtro_marcas.iloc[5:35,:].copy()


marca_a= sec_marca.filter(items = ["titulo","marca"])

marca_a.groupby('titulo').count()["marca"].plot(kind='bar',stacked=True,title="Total")



filtro_val = df_aparatos.filter(items = ["titulo","opiniones"]).sort_values('opiniones', ascending=False).head(24)


titulos = np.unique(filtro_val['titulo'].get_values(), return_counts = True)[0]
num_opiniones = filtro_val['opiniones'].get_values()

posicion_y = np.arange(len(num_opiniones))
plt.figure(figsize=(5,15))
plt.barh(posicion_y, num_opiniones, align = "center")
plt.yticks(posicion_y, titulos)
plt.xlabel('Valoracion', fontsize=15)
plt.title("Cantidad de valoracion del vendedor por producto", fontsize=15)
for i, v in enumerate(num_opiniones):
    plt.text(v + 3, i, str(v),fontsize='x-large')
plt.show()