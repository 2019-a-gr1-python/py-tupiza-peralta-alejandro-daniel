# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 21:46:32 2019

@author: ad_tp
"""

import pandas as pd
import os

path_impresoras = 'C:/Users/ad_tp/OneDrive/Documentos/GitHub/py-tupiza-peralta-alejandro-daniel/Deberes/Proyecto/proyecto_scrapy/scrapyP/impresoras_items.csv'

columnas_a_usar = ['titulo','modelo','marca',
                  'precio','condicion','opiniones',
                   'tipo_vendedor','ventas_vendedor']

df_impresoras = pd.read_csv(
        path_impresoras,
        usecols=columnas_a_usar,
        index_col='titulo'
        )

precio = df_impresoras.filter(items = ["titulo","precio"]).sort_values('precio', ascending=False)
