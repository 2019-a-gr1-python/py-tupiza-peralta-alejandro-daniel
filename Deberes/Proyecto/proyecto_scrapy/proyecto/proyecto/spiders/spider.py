# sys.setdefaultencoding('utf8')

import scrapy
from scrapy.spider import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from proyecto.items import ProyectoItem

class ComputadorasSpider(CrawlSpider):
	name = 'computadoras'
	item_count = 0
	allowed_domain = ['www.mercadolibre.com.mx']
	start_urls = ['https://listado.mercadolibre.com.mx/computadoras#D[A:computadoras,L:1]']

	rules = {
		# Para cada item
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="pagination__next"]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//h2[contains(@class,"item__title")]/a')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		computadora_item = ProyectoItem()
		#info de producto
		computadora_item['titulo'] = response.xpath('normalize-space(//h1[@class="item-title__primary "]/text())').extract_first()
		computadora_item['modelo'] = response.xpath('normalize-space(//*[@id="root-app"]/div[2]/div[1]/div[1]/section[3]/div/section/ul/li[3]/span)').extract()
		computadora_item['marca'] = response.xpath('normalize-space(//*[@id="root-app"]/div[2]/div[1]/div[1]/section[3]/div/section/ul/li[1]/span)').extract()
		computadora_item['precio'] = response.xpath('normalize-space(//span[@class="price-tag-fraction"]/text())').extract()
		computadora_item['condicion'] = response.xpath('normalize-space(//div[@class="item-conditions"]/text())').extract()
		computadora_item['opiniones'] = response.xpath('normalize-space(//span[@class="review-summary-average"]/text())').extract()
		#info de la tienda o vendedor
		computadora_item['tipo_vendedor'] = response.xpath('normalize-space(//p[contains(@class, "power-seller")]/text())').extract()
		computadora_item['ventas_vendedor'] = response.xpath('normalize-space(//dd[@class="reputation-relevant"]/strong/text())').extract()
		
		self.item_count += 1
		if self.item_count > 40:
			raise CloseSpider('item_exceeded')
		yield computadora_item