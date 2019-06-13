# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 07:22:48 2019

@author: Alejo
"""

import pandas as pd
import numpy as np
import os
import sqlite3

path_guardado = 'C:/Users/Alejo/Documents/Documentos_U/Python/py-tupiza-peralta-alejandro-daniel/03_Pandas/data/csv/artwork_data.pickle'

df_completo_pickle = pd.read_pickle(path_guardado)

df = df_completo_pickle.iloc[49980:50019,:].copy()


# Tipos de archivos
# - JSON
# - SQL
# - EXCEL



######################### Excel ###########################

df.to_excel('ejemplo_basico.xlsx')

df.to_excel('ejemplo_basico_sin_indices.xlsx', index=False)

columnas = ['artist','title','year']

df.to_excel('columnas.xlsx', columns = columnas)


# Multiples hojas de trabajos (worksheet)

writer = pd.ExcelWriter('multiples_worksheet.xlsx',
                        engine = 'xlsxwriter')

df.to_excel(writer, sheet_name = 'Preview')

df.to_excel(writer, sheet_name = 'Preview Dos', index = False)

df.to_excel(writer, sheet_name = 'Preview Tres', columns = columnas)

writer.save()

# Formateo Condicional

artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('colores.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': '2_color_scale',
        'min_value': '10',
        'min_type': 'percentile',
        'max_value': '99',
        'max_type': 'percentile'
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()


######################### SQL ###########################

with sqlite3.connect('bdd_python.db') as conexion:
    df.to_sql('tabla', conexion)

## with mysql.connect('mysql://user:password@ip:puerto/bd') as conexion:
##     df.to_sql('Alguien', conexion)>


######################### JSON ###########################

df.to_json('artistas.json')
    
df.to_json('artistas_orientado_tabla.json', orient = 'table')

################### FORMATO DATA_BAR ######################

artistas_contados = df_completo_pickle['artist'].value_counts()

writer = pd.ExcelWriter('formato_data_bar.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

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

writer.save()

################### FORMATO incon_set ######################

artistas_contados = df['artist'].value_counts()

writer = pd.ExcelWriter('formato_icon_set.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B1:{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': 'icon_set',
        'icon_style': '5_quarters'
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()

################### FORMATO quarters ######################

artistas_contados = df_completo_pickle['artist'].value_counts().head(100)

writer = pd.ExcelWriter('formato_bar_right.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        #'type': 'icon_set',
        #'icon_style': '5_ratings'
        'type': 'icon_set',
        'icon_style': '5_quarters'
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()

####################### arrow ###################
artistas_contados = df_completo_pickle['artist'].value_counts().head(100)

writer = pd.ExcelWriter('formato_arrow.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': 'icon_set',
        'icon_style': '5_arrows_gray'
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()

################################## ICON SET 2 ############33333########

artistas_contados = df_completo_pickle['artist'].value_counts().head(100)

writer = pd.ExcelWriter('formato_icon.xlsx', engine = 'xlsxwriter')

artistas_contados.to_excel(writer, sheet_name = 'Artistas contados')

hoja_artistas = writer.sheets['Artistas contados']

rango_celdas = 'B2:B{}'.format(len(artistas_contados.index) + 1)

formato = {
        'type': 'icon_set',
        'icon_style': '4_red_to_black',
        'icons': [{'criteria': '>=', 'type': 'number',     'value': 90},
                  {'criteria': '<',  'type': 'percentile', 'value': 50},
                  {'criteria': '<=', 'type': 'percent', 'value': 25}]
        }

hoja_artistas.conditional_format(rango_celdas, formato)

writer.save()






    