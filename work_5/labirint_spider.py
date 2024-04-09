import scrapy

class LabirintSpider(scrapy.Spider):
    name = 'labirint_spider'
    start_urls = ['https://www.labirint.ru/genres/2304/']

    def parse(self, response):
        books = response.css('.product-title-link::text').getall()
        
        yield {
            'books': books
        }
