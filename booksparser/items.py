# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooksparserItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    annotation = scrapy.Field()
    url = scrapy.Field()
    _id = scrapy.Field()

