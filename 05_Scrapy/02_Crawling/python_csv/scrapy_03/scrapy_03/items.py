# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import re
from scrapy.loader.processors import MapCompose
from scrapy.loader.processors import TakeFirst

def transformar_url_imagen(texto): 
    url = 'https://www.fybeca.com' 
    cadena_a_reemplazar = '../..'   
    return texto.replace(cadena_a_reemplazar,url)

def FiltrarPrecio(precio):
    precio = re.findall(r"\d+\.\d+", precio)    
    return float(str(precio[0]))
    
class ProductoFybeca(scrapy.Item):
    imagen = scrapy.Field(
        input_processor = MapCompose(
            transformar_url_imagen
            ),
        output_processor = TakeFirst()
    )
    titulo = scrapy.Field()
    precio = scrapy.Field(
        input_processor = MapCompose(
            FiltrarPrecio
        )
    )