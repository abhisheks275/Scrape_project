import scrapy


class SuperheroApiSpider(scrapy.Spider):
    name = 'superhero_api'
    allowed_domains = ['https://superheroapi.com/api/access-token']
    start_urls = ['https://superheroapi.com/api/']

    def parse(self, response):
     print(response.body)
