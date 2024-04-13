import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CrawlingSpider(CrawlSpider):
    name = 'mycrawler'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_common_misconceptions',
    ]

    custom_settings = {
        "CLOSESPIDER_PAGECOUNT": 200, #max_pages
        "DEPTH_LIMIT": 6, #max_depth
    }
    
    rules = (
        Rule(LinkExtractor(allow=('/wiki/', ), deny=('/wiki/Category', '/wiki/Help', '/wiki/Portal', '/wiki/Talk', '/wiki/Wikipedia', '/wiki/Template', )), callback='parse', follow=True),
    ) # deny/drop unrelated sites

    def parse(self, response): 
        file_name = response.url.split("/")[-1] + '.html' # url name + html
        with open(file_name, 'wb') as f: #save as html 
            f.write(response.body)

#https://www.youtube.com/watch?v=m_3gjHGxIJc&ab_channel=NeuralNine