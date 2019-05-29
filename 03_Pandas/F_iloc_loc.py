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

a = df['width'].sort_values()



