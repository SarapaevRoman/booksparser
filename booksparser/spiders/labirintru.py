import scrapy
from scrapy.http import HtmlResponse
from booksparser.items import BooksparserItem


class LabirintruSpider(scrapy.Spider):
    name = "labirintru"
    allowed_domains = ["labirint.ru"]
    start_urls = ["https://www.labirint.ru/genres/2791/"]

    def parse(self, response: HtmlResponse):

        links = response.xpath("//a[@class='product-title-link']/@href").getall()
        for link in links:
            yield response.follow(link, callback=self.book_parse)
                
        next_page = response.xpath("//a[@class='pagination-next__text']/@href").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        
    def book_parse(self, response: HtmlResponse):

        title = response.xpath("//h1/text()").get(default="").strip()
        price = response.xpath("//span[@class='buying-pricenew-val-number']/text()").get(default="").strip()
        annotation = response.xpath("//div[@id='product-about']//text()").getall()
        annotation = " ".join([line.strip() for line in annotation if line.strip()])
        url = response.url
        yield BooksparserItem(title=title, price=price, annotation=annotation, url=url)
            
        
