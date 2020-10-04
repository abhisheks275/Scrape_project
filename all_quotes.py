import scrapy


class AllQuotesSpider(scrapy.Spider):
    name = 'all_quotes'
    allowed_domains = ['allauthor.com/quotes/']
    start_urls = ['https://allauthor.com/quotes/59421//']

    def parse(self, get):
     quotes = get.xpath("//h1").getall()
     yield
     {
         'quotes': quotes
     }
     






      