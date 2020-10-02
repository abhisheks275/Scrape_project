# -*- coding: utf-8 -*-
import scrapy
import json

class ScrapQuotesSpider(scrapy.Spider):
    name = 'scrap_quotes'
    allowed_domains = ['www.allauthor.com/quotes/']
    start_urls = ['http://www.allauthor.com/quotes//']

    def parse(self, response):
        response.get('quotesimage')

        