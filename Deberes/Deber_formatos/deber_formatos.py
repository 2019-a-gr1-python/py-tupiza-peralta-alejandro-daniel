# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:22:57 2019

@author: Alejo
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = 'C:/Users/Alejo/Documents/Documentos_U/Python/py-tupiza-peralta-alejandro-daniel/03_Pandas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

df = df_completo_pickle.iloc[49980:50019,:].copy()

writer = pd.ExcelWriter('multiples_formatos.xlsx', engine = 'xlsxwriter')

artistas_contados = df_completo_pickle['artist'].value_counts()

###################### DATA BAR ########################################

artistas_contados.to_excel(writer, sheet_name = 'Data Bar')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': 'data_bar',
        'min_value': '10',
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile',
        'bar_color': 'green'
        }

hoja_artistas.conditional_format(rango_celdas, formato)

artistas_contados = df['artist'].value_counts()

################### FORMATO incon_set ######################

df.to_excel(writer, sheet_name = 'Icon Set')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B1:{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': 'icon_set',
        'icon_style': '5_quarters'
        }

hoja_artistas.conditional_format(rango_celdas, formato)


df.to_excel(writer, sheet_name = 'Ratings')

writer.save()