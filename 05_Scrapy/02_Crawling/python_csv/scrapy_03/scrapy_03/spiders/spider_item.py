import scrapy
from scrapy_03.items import ProductoFybeca
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst

# 1) Generar las URLS
# 2) Anadir el precio (clase, input, ouput)
# 3) Transformar el precio a numero (float)
# 4) Expotar a csv
# 5) Anadir un pipeline para seleccionar los productos mayores al precio promedio

class AraniaProductosFybeca(scrapy.Spider):
    name = 'arania_fybeca'

    def start_requests(self):
        urls = []
        for i in range(0, 151, 25):
            urls.append(f'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?s={i}&pp=25&cat=238&ot=0')

        for url in urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):

        #precio = response.css('.price::attr(data-bind)')
        productos = response.css('div.product-tile-inner')
        for producto in productos:
            existe_producto = len(producto.css('div.detail'))
            if(existe_producto > 0):
                # titulo = producto.css('a.name::text')
                # url = producto.xpath('//div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src')
                producto_loader = ItemLoader(
                    item = ProductoFybeca(),
                    selector = producto
                )
                
                producto_loader.default_output_processor = TakeFirst()

                producto_loader.add_css(
                    'titulo',
                    'a.name::text'
                )

                producto_loader.add_css(
                    'precio',
                    '.price::attr(data-bind)'
                )

                producto_loader.add_xpath(
                    'imagen',
                    'div[contains(@class,"detail")]/a[contains(@class,"image")]/img[contains(@id,"gImg")]/@src'
                )

                #producto_imprimir = producto_loader.load_item()
                #print(producto_imprimir)
                yield producto_loader.load_item()
        
'''        precios = response.css('.price::attr(data-bind)')
        for precio in precios:
            existe _precio = len()
            if(existe_producto > 0 ):
                precio_loader = ItemLoader(
                    item = PrecioFybeca(),
                    selector = precio
                )

                precio_loader.default_output_processor = TakeFirst()

                precio_loader.add_css(
                    'precio',
                )'''