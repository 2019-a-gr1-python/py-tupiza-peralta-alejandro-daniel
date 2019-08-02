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
    dato_nuevo=dato_nuevo.replace('-', ' ')
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



coordenadas = ['-3.983822, -79.207831','-0.946716, -80.722219','-0.259688, -79.189111','-2.135178, -79.903493','-2.186876, -79.893622',
               '-2.200553, -79.900288','-0.183597, -78.481303','-0.101247, -78.479305','-0.101247, -78.479305','-0.134944, -78.481752',
               '-0.101247, -78.479305','-0.099632, -78.466817','-0.206460, -78.480151','-1.035525, -80.467248','-0.164774, -78.467792',
               '-1.653530, -78.666495','-1.653487, -78.666495','-0.194034, -78.491601',
               '-0.134944, -78.481752','-0.126546, -78.480757','-0.139089, -78.493190','-0.216855, -78.488372','-0.237047, -78.485869',
               '0.342826, -78.122625','0.328318, -79.472235','-0.129179, -78.496872','-0.310616, -78.546209','-0.065822, -78.462245',
               '-0.211076, -78.509862','40.489523, -3.680884','-0.097950, -78.435439','-0.297207, -78.461294','-0.236466, -78.530079']

latitud = []
longitud = []
for x in coordenadas:
    coord = x.split(',')
    latitud.append(coord[0])
    longitud.append(coord[1])

df_empresas['Latitud direccion'] = latitud
df_empresas['Longitud direccion'] = longitud


path_final='C:/Users/ad_tp/OneDrive/Documentos/GitHub/py-tupiza-peralta-alejandro-daniel/Deberes/Examen_IIB/empresas_final/empresas.xlsx'
df_empresas.to_excel(path_final)


###################