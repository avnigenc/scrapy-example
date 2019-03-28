import scrapy

class AutomartcoItem(scrapy.Item):
    id = scrapy.Field()
    url = scrapy.Field()
    content = scrapy.Field()
    make = scrapy.Field()
    model = scrapy.Field()
    version = scrapy.Field()
    price = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    date = scrapy.Field()
    color = scrapy.Field()
    year = scrapy.Field()
    mileage = scrapy.Field()
    door = scrapy.Field()
    transmission = scrapy.Field()
    power = scrapy.Field()
    engine_size = scrapy.Field()
    body_type = scrapy.Field()
    is_new = scrapy.Field()
    pictures = scrapy.Field()

class CollectLinks(scrapy.Item):
    url = scrapy.Field()
