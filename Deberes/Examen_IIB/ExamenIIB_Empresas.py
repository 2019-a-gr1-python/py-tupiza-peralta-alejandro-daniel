# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 23:10:07 2019

@author: ad_tp
"""

import pandas as pd
import numpy as np

# DataFrame de INFORMACION DISTR. para Empresas
df_info = pd.read_excel('C:/Users/ad_tp/OneDrive/Documentos/GitHub/py-tupiza-peralta-alejandro-daniel/Deberes/Examen_IIB/documentos_iniciales/informacion_general.xlsx',sheet_name='INFORMACIÓN DISTR.',skiprows=3)

# DataFrame de REVENTA para Empresas
df_reventa = pd.read_excel('C:/Users/ad_tp/OneDrive/Documentos/GitHub/py-tupiza-peralta-alejandro-daniel/Deberes/Examen_IIB/documentos_iniciales/informacion_general.xlsx',sheet_name='REVENTA',skiprows=1)

# Renombrar las columnas del df_info
df_info.rename(columns={
                   'Unnamed: 0': 'Codigo',
                   'Unnamed: 1': 'Nombre',
                   'Unnamed: 2': 'Direccion',
                   'Unnamed: 3': 'Telefono',
                   'Unnamed: 4': 'Representante',
                   'Unnamed: 5': 'Correo',
                   'Unnamed: 6': 'Ruc'}, inplace=True)

# listas donde se van a llenar los datos de los dos dataframes
Codigo = []
Nombre = []
Telefono = []
Representante = []
Ruc = []
    
# Llenado de datos en las listas del df_info
i=0
for row in df_info['Nombre']:
        
    Codigo.append(df_info['Codigo'][i])
    Nombre.append(df_info['Nombre'][i])
    Telefono.append(df_info['Telefono'][i])
    Representante.append(df_info['Representante'][i])
    Ruc.append(df_info['Ruc'][i])
    
    i=i+1



# Llenado de datos en las listas del df_reventa
i=0
for row in df_reventa['NOMBRE DEL CLIENTE']:
        
    Codigo.append(df_reventa['CÓDIGO'][i])
    Nombre.append(df_reventa['NOMBRE DEL CLIENTE'][i])
    Telefono.append(df_reventa['TELÉFONO '][i])
    Representante.append(df_reventa['NOMBRE DEL REPRESENTATE  LEGAL'][i])
    Ruc.append(df_reventa['RUC'][i])
    
    i=i+1


# Diccionario de datos de los dos DataFrames
dfdicEmp={
    'Codigo' : Codigo,
    'Nombre' : Nombre,
    'Ruc' : Ruc,
    'Representante legal' : Representante,
    'Telefono' : Telefono,
}

# DataFrame final
df_empresas = pd.DataFrame(dfdicEmp)
df_empresas.set_index("Codigo")

# Funcion para limpiar los datos
def limpiar_datos(dato):
    dato_nuevo=dato
    dato_nuevo=dato_nuevo.replace('|','nan')
    dato_nuevo=dato_nuevo.replace('´',' ')
    dato_nuevo=dato_nuevo.replace('\n ', ' ')
    return dato_nuevo


# limpiar telefonos
limp_tel=df_empresas['Telefono'].values
limp_tel=list(map(limpiar_datos,limp_tel))
df_empresas['Telefono']=limp_tel
df_empresas

# limpiar ruc
limpiar_ruc = df_empresas['Ruc'].values
limpiar_ruc=list(map(limpiar_datos,limpiar_ruc))
df_empresas['Ruc']=limpiar_ruc
df_empresas



path_final='C:/Users/ad_tp/Documentos/empresas.xlsx'
df_empresas.to_excel(path_final)


###################