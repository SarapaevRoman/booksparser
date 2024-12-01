# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from itemadapter import ItemAdapter
from pymongo import MongoClient


class BooksparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.books
    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        adapter = ItemAdapter(item)
        collection.insert_one(adapter.asdict())
        
        return item
    
class JsonWriterPipeline:
    def open_spider(self, spider):
        # Открытие файла для записи, добавление символа [
        self.file = open("labirint_books.json", "w", encoding="utf8")
        self.file.write("[")

    def close_spider(self, spider):
        # Завершаем файл JSON, добавляем символ ]
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        # Преобразуем объект item в строку JSON
        line = json.dumps(item, ensure_ascii=False, indent=4) + ",\n"
        self.file.write(line)
        return item
