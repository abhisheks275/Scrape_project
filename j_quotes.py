import scrapy
import json 

class JQuotesSpider(scrapy.Spider):
    name = 'j_quotes'
    start_urls = ['https://allauthor.com/quotes/']
    headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cookie": "aakey=BNVezgGWoRa3yPBRDPBN; _gcl_au=1.1.16710339.1601419066; _ga=GA1.2.1455372434.1601419066; _gid=GA1.2.269516394.1601419066; cookieconsent_dismissed=yes; _fbp=fb.1.1601504999711.1935119445; refer=allauthor.com; PHPSESSID=aldbc66v5h9lc00urf72ir49q4",
    "referer": "https://allauthor.com/quotes/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
    }
    def parse(self, response):
        url = 'https://allauthor.com/getQuotesDirectory.php?draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false&orderby=usersView%20desc&status=Y&category=&author=&_=1601680327401'
        request = scrapy.Request(url, callback=self.parse_api, headers = self.headers)
        
        def parse_api(self,response):
            base_url = 'https://allauthor.com/getQuotesDirectory.php?draw=1&columns%5B0%5D%5Bdata%5D=0&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=50&search%5Bvalue%5D=&search%5Bregex%5D=false&orderby=usersView%20desc&status=Y&category=&author=&_=1601680327401'
            raw_data = response.body
            data = json.loads(raw_data)
            for quotes in data:
                quote_data = quotes['aaData']
                quote_url = base_url+quote_data
                request = scrapy.Request(school_url, callback=self.parse_quotes, headers=self.headers)
                yield request 

            def parse_api(self,response):
                raw_data = response.body
                data = json.loads(raw_data)
                yield 
                {
                    'quotes' : data['aaData']
                }


