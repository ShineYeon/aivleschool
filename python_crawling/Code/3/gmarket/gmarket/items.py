
import scrapy

#scrapy.Item의 상속을 받음
class GmarketItem(scrapy.Item) :
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
