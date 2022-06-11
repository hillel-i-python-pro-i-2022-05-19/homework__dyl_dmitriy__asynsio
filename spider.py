import scrapy

from scrapy import signals
from scrapy.http import Request
from scrapy.utils.trackref import object_ref
from scrapy.utils.url import url_is_from_spider

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


#https://www.yakaboo.ua/ua/knigi.html
#https://www.yakaboo.ua/ua/knigi/hudozhestvennaja-literatura.html
#https://www.yakaboo.ua/ua/knigi/hudozhestvennaja-literatura/detektiv.html

class BookSpider(CrawlSpider):
    name = "all_books"
    start_urls = ["https://www.yakaboo.ua/"]

    rules = (
        Rule(LinkExtractor(allow="knigi")),
        Rule(LinkExtractor(allow="hudozhestvennaja-literatura"), callback="parse_items")
    )


    def parse_items (self, response):
        yield{
            "First":response.css('a.breadcrumbs__link.smartLink span::text')[1].get().strip(),
            "Second":response.css('a.breadcrumbs__link.smartLink span::text')[2].get().strip(),
            #"Third":response.css('a.breadcrumbs__link.smartLink span::text')[3].get().strip()
            "name": response.css('h1.product-detail-page__title::text').get().strip(),

            "buy": response.css('p.product-detail-page__purchased-text::text').get().split()[1],

        }


