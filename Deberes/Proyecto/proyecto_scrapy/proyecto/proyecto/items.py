# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProyectoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #info de producto
    titulo = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    opiniones = scrapy.Field()

    #info de la tienda o vendedor
    tipo_vendedor = scrapy.Field()
    ventas_vendedor = scrapy.Field()
