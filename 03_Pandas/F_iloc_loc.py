# -*- coding: utf-8 -*-
"""
Created on Wed May 29 07:35:53 2019

@author: Alejo
"""

import pandas as pd

path_guardado = 'C:/Users/Alejo/Documents/Documentos_U/Python/py-tupiza-peralta-alejandro-daniel/03_Pandas/data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

primero = df.loc[1035,'artist']
segundo = df.loc[1036,'units']

df.loc[0]   # Error porque no esta dentro del label indice

primero_a = df.iloc[0,1]

primero_b = df.iloc[0,:]

primero_c = df.iloc[0:100,2:4]

tres_primeros = df.head(10)['width'].sort_values(ascending=False).head(3)

tres_ultimos = df.head(10)['width'].sort_values().tail(3)

a = df['year'].sort_values(axis=0)

serie_validado = pd.to_numeric(df['width'], errors='coerce')

df.loc[:,'width'] = serie_validado
df.iloc[:,5] = serie_validado

diez_primeros = df['width'].sort_values(ascending=False).head(10)

diez_ultimos = df['width'].sort_values(ascending=False).tail(10)

serie_validado_height = pd.to_numeric(df['height'], errors='coerce')
df.loc[:,'height'] = serie_validado_height


