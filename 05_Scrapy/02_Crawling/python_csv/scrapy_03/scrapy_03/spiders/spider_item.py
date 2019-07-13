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
        '''urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=0&pp=25'
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=25&pp=25'
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=50&pp=25'
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=75&pp=25'
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=100&pp=25'
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=125&pp=25'
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=150&pp=25'
        ]'''
        urls = get_urls() 
        for url in urls:
            yield scrapy.Request(url=url)
            
    def parse(self, response):

        #precios = response.css('.price::attr(data-bind)')
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

def get_urls():
    base_url = 'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=238&s=changeThis&pp=25'
    return [base_url.replace('changeThis',str(url)) for url in range(0,150,25) ]