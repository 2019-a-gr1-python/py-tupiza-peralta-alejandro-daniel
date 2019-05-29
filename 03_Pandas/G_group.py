# -*- coding: utf-8 -*-
"""
Created on Wed May 29 08:23:10 2019

@author: Alejo
"""

import pandas as pd
import numpy as np
import math

path_guardado = 'C:/Users/Alejo/Documents/Documentos_U/Python/py-tupiza-peralta-alejandro-daniel/03_Pandas/data/csv/artwork_data.pickle'

df = pd.read_pickle(path_guardado)

seccion_df = df.iloc[49980:50019,:].copy()

df_agrupado_ay = seccion_df.groupby('artist')

type(df_agrupado_ay)

for acquisitionYear, registros in df_agrupado_ay:
    print(acquisitionYear)
    # print(registros)
    
def llenar_valores_vacios(series):
    valores = series.value_counts()
    if(valores.empty):
        return series
    '''
    # 1) iterar y sumar los valores
    sumatoria = 0
    numero_nans = 0
    for valor in series:
        print(valor)
        print(type(valor))
        if type(valor) == str:
            sumatoria = sumatoria + int(valor)
        if type(valor) == float:
            numero_nans = numero_nans + 1
    print(sumatoria)
    
    # 2) Dividir para el numero de valores
    division = series.size - numero_nans
    valor_mas_utilizado = sumatoria / division
    print(valor_mas_utilizado)
    '''
    nuevo_valor = series.fillna(valores.index[0])
    return nuevo_valor

def transformar_df(df):
    df_artist = df.groupby('artist')
    arreglo_df_grupo = []
    
    for nombre_artista, registros_agrupados in df_artist:
        copia = registros_agrupados.copy()
        serie_medium = registros_agrupados['medium']
        serie_units = registros_agrupados['units']
        copia.loc[:,'medium'] = llenar_valores_vacios(serie_medium)
        copia.loc[:,'units'] = llenar_valores_vacios(serie_units)
        arreglo_df_grupo.append(copia)
        
    nuevo_df_transformado = pd.concat(arreglo_df_grupo)
    return nuevo_df_transformado

seccion_df_t = transformar_df(seccion_df)