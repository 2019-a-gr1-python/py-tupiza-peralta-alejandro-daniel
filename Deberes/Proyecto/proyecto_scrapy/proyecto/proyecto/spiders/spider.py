import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from proyecto.items import ProyectoItem

class ProyectoItem(CrawlSpider):
    name = 'proyecto'
    item_count = 0
    allowed_domain = ['https://computacion.mercadolibre.com.ec']
    start_urls = ['https://computacion.mercadolibre.com.ec/apple-equipos/']

    rules = {

        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="andes-pagination__button"]/a'))),
        Rule(LinkExtractor(allow = (), restrict_xpaths = ('//h2[@class="item__title list-view-item-title"]')),
                            callback = 'parse_item', follow = False)
    }

    """ 
        segundo
        //h2[@class="item__title list-view-item-title"]/a
        //*[contains(@class, "list-view-item-title")]
    """
    
    """
        primero
        //*[contains(@class, "andes-pagination__button--next")]
        //li[@class="andes-pagination__button andes-pagination__button--next"]
    """

    def parse_item(self, response):
        item_apple = ProyectoItem()

        #infor de producto
        item_apple['titulo'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/header/h1/text())').extract()
        item_apple['pubicacion'] = response.xpath('normalize-space(//span[@class="item-info__id-number"]/text())').extract()
        item_apple['precio'] = response.xpath('normalize-space(//*[@id="productInfo"]/fieldset[1]/span/span[2]/text())').extract()
        item_apple['condicion'] = response.xpath('normalize-space(//*[@id="short-desc"]/div/dl/div/text())').extract()
        item_apple['envio'] = response.xpath('normalize-space(//*[contains(@class,"shipping-method-title")/text()])').extract()
        item_apple['ubicacion'] = response.xpath('normalize-space(//*[@id="productInfo"]/div[1]/fieldset[2]/article/div[1]/p[2]/text())').extract()
   
        # Jefe de la tienda o vendedor
        item_apple['tipo_vendedor'] = response.xpath('normalize-space(//*[@id="root-app"]/div/div[1]/div[2]/div[1]/section[2]/div[2]/p[1]/text())').extract()
        item_apple['reputacion'] = response.xpath('normalize-space(//*[@id="root-app"]/div/div[1]/div[2]/div[1]/section[2]/div[3]/div/div/div/dl/dd[1]/strong/text())').extract()
        item_apple['ventas_vendedor'] = response.xpath('normalize-space(//*[@id="root-app"]/div/div[1]/div[2]/div[1]/section[2]/div[3]/div/div/div/dl/dd[3]/strong/text())').extract()

        self.item_count += 1
        if self.item_count > 20:
            raise CloseSpider('item_exceeded')
        yield item_apple