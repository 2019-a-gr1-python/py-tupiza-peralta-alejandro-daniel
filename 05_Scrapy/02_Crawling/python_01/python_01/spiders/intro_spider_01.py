import scrapy
import pandas as pd

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/category/books_1/page-1.html'
        ]

        for url in urls:
            yield scrapy.Request(url=url)

    def parse(self, response):
        etiqueta_contenedor = response.css('article.product_pod')

        titulos = etiqueta_contenedor.css('h3 > a::attr(title)').extract()

        stocks = etiqueta_contenedor.css('div.product_price > p.instock.availability::text').extract()

        precios = etiqueta_contenedor.css('div.product_price > p.price_color::text').extract()

        diccionario = {'titulos' : titulos, 'stocks ' : stocks, 'precios' : precios}
     
        print(titulos)
        print(stocks)
        print(precios)

        print(diccionario)

        df_archivo = pd.DataFrame([key, diccionario[key] for key in diccionario.keys()], columns=['titulos','stocks','precios'])
        df_archivo

        df.to_excel('libros.xlsx')