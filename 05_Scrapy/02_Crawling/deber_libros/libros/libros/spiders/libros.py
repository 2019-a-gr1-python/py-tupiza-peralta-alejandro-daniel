import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class araniaCrawlLibro(CrawlSpider):
    name = 'crawl_libro'
    allowed_domains = [  # Heredado (conservar nombre)
        'http://books.toscrape.com/'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'http://books.toscrape.com/'
    ]
    # Heredado (conservar nombre)


    url_segmento_permitido = (
        '/catalogue/category/books/mystery_3/',
        '/catalogue/category/books/fantasy_19/' 
    )


    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido
            ), callback='parse_page')
        ,
    )

    rules = regla_dos


    def parse_page(self, response):
        lista_libros = response.css('article.product_pod > h3 > a::attr(title)').extract()

        for libreria in lista_programas:
            with open('libros.txt', 'a+') as archivo:
                archivo.write(libreria + '\n')