import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrawlOnu(CrawlSpider):
    name = 'crawl_libros'  # Heredado (conservar nombre)
    
    allowed_domains = [  # Heredado (conservar nombre)
        'http://books.toscrape.com/'
    ]
    start_urls = [  # Heredado (conservar nombre)
        'https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/index.html'
    ]
    # Heredado (conservar nombre)

    regla_uno = (
        Rule(LinkExtractor(), callback='parse_page')
        ,
    )

    url_segmento_permitido = (
        '/catalogue/category/books/mystery_3/',
        '/catalogue/category/books/fantasy_19/' 
    )

    url_segmento_restringido = (
        
    )

    regla_dos = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido
            ), callback='parse_page')
        ,
    )

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains=allowed_domains,
                allow=url_segmento_permitido,
                deny=url_segmento_restringido
            ), callback='parse_page')
        ,
    )

    rules = regla_dos


    def parse_page(self, response):
        lista_programas = response.css('article.product_pod > h3 > a::attr(title)').extract()

        for agencia in lista_programas:
            with open('libros.txt', 'a+') as archivo:
                archivo.write(agencia + '\n')