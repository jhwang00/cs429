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
        "CLOSESPIDER_PAGECOUNT": 50, #max_pages
        "DEPTH_LIMIT": 3, #max_depth
    }
    
    rules = (
        Rule(LinkExtractor(allow=('/wiki/', ), deny=('/wiki/Category', '/wiki/Help', '/wiki/Portal', '/wiki/Talk', '/wiki/Wikipedia',)), callback='parse', follow=True),
    )

    def parse(self, response):
        #datas = response.xpath("//ul").getall()
        #yield {'url': response.url}
        file_name = response.url.split("/")[-1] + '.html'
        #print(type(response.body))
        #html_content = "<!-- URL: " + response.url + " -->\n" + response.body
        with open(file_name, 'wb') as f:
            f.write(response.body)

#https://www.youtube.com/watch?v=m_3gjHGxIJc&ab_channel=NeuralNine