"""This will scrape the page 1 and page 2 of the mentioned
URLS and scrape their body's html code in a seperate file
using scrapy spider
"""
"""
Use command 'scrapy crawl qoutes' to crawl the webpages. 
"""

import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html' %page

        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('saved file %s' %filename)