import scrapy
from ..items import AutomartcoItem
from ..items import CollectLinks

from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from w3lib.html import remove_tags

class carSpider(CrawlSpider):
    name = 'car'
    allowed_domains = ['https://www.automart.co.za/']
    start_urls = ['https://www.automart.co.za/cars/']
    
    rules = (
        Rule(LinkExtractor(allow=(), restrict_xpaths=".pagination.pagination-sm > li:nth-child(n) > a::attr(href)"), follow=True),
        Rule(LinkExtractor(restrict_xpaths=".card.p-b-sm > div > h3 a::attr(href)"), callback="parse_car")
    )


    def parse_car(self, response):

        car_loader = ItemLoader(item=AutomartcoItem(), response=response)
        car_loader.default_input_processor = MapCompose(remove_tags)
        car_loader.default_output_processor = TakeFirst()


        car_loader.add_css("id", "#adID")
        car_loader.add_css("content", ".bold")

        car_loader.add_css("make", ".bread-bottom li:nth-child(4) a")
        car_loader.add_css("model", ".bread-bottom li:nth-child(5) a")
        car_loader.add_css("version", ".bold")

        car_loader.add_css("price", ".price")
        car_loader.add_css("city", "#mobile-link-wrapper:nth-child(6) .muted+ span")
        car_loader.add_css("district", ".bold")
        car_loader.add_css("date", ".text-left")
        car_loader.add_css("color", ".co")
        car_loader.add_css("year", ".ye")
        car_loader.add_css("mileage", ".mi")
        car_loader.add_css("door", "")
        car_loader.add_css("fuel", ".ft")
        car_loader.add_css("tranmission", ".tr")
        car_loader.add_css("power", "")
        car_loader.add_css("engine_size", ".en")
        car_loader.add_css("body_type", "")
        car_loader.add_css("is_new", ".ct")
        car_loader.add_css("pictures", ".carousel-inner img::attr(src)")

        yield car_loader.load_item()
            