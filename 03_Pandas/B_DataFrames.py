# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:37:01 2019

@author: Alejo
"""

import numpy as np
import pandas as pd
#array randomico
arr_rand = np.random.randint(0,10,6).reshape(2,3)
df = pd.DataFrame(arr_rand,
                  columns=['Estatura (cm)','Peso (gr)','Edad (anios)'])

df2 = pd.DataFrame(arr_rand)
df3 = pd.DataFrame(arr_rand)

df2.columns = ['Estatura (cm)','Peso (gr)','Edad (anios)']

df3[0] # No es el indice
df2['Estatura (cm)'] # Es el nombre de la columna
type(df2['Estatura (cm)'])

df2['Estatura (cm)'][0]