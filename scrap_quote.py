import scrapy
import json

class ScrapQuoteSpider(scrapy.Spider):
    name = 'scrap_quote'
    allowed_domains = ['https://allauthor.com/quotes/']
    start_urls = ['https://allauthor.com/quotes//']

    def parse(self, response):
        print(response.body)
