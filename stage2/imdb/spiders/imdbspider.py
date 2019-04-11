# coding:utf-8

from scrapy.spiders import CrawlSpider, Request, Rule
from imdb.items import ImdbItem
from scrapy.linkextractors import LinkExtractor


class ImdbSpider(CrawlSpider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com']
    rules = (
        Rule(LinkExtractor(allow=r"/title/tt\d+$"), callback="parse_imdb", follow=True),
    )

    def start_requests(self):
        # for i in range(1, 3051, 50):
        #     url = "https://www.imdb.com/search/title?title_type=feature&release_date=2018-05-01,2019-05-01&start=" + str(i)
        #     yield Request(url=url, callback=self.parse)
        url = "https://www.imdb.com/search/title?title_type=feature&release_date=2018-05-01,2019-05-01"
        yield Request(url=url, callback=self.parse)

    def parse_imdb(self, response):
        item = ImdbItem()
        try:
            item['url'] = response.url
            item['video_title'] = "".join(response.xpath('//*[@class="title_wrapper"]/h1/text()').extract())
            item['video_year'] = "".join(response.xpath('//*[@id="titleYear"]/a/text()').extract())
            item['video_level'] = "".join(response.xpath('//*[@class="subtext"]/a[1]/text()').extract())
            item['video_length'] = "".join(response.xpath('//*[@class="subtext"]/a[2]/text()').extract())
            item['video_genres'] = "".join(response.xpath('//*[@class="subtext"]/a[3]/text()').extract())
            item['video_releasedate'] = "".join(response.xpath('//*[@class="subtext"]/a[4]/text()').extract())
            yield item
        except Exception as error:
            print(error)+
