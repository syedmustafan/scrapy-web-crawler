"""This will scrape the quotes of a webpage in a json file seperately
"""
"""
Use command 'scrapy crawl qoute1 -o quotes.json' to crawl the webpages. 
"""
import scrapy

class QuoteSpider2(scrapy.Spider):
    name = 'quote1'

    start_urls = ["http://quotes.toscrape.com/page/1/",
    'http://quotes.toscrape.com/page/2/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get()
            }