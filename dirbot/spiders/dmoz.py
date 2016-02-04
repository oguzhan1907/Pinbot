from scrapy.spiders import Spider
from scrapy.selector import Selector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["https://www.pinterest.com/"]
    start_urls = ["https://www.pinterest.com/Girl_in_Dublin/followers/"]

    def __init__(self,*args,**kwargs):
        super(DmozSpider, self).__init__( *args, **kwargs)
        self.download_delay = 6.0

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        #sel = Selector(response)
        accounts = response.xpath('//a[@class="userWrapper"]')
        items =[]

        for user in accounts:
            item = Website()
            item['usr_name'] = user.xpath('./@href').extract()[0]
            item['pins'] = user.xpath('.//p[@class="userStats"]/span[@class="value"]/text()').extract()[0]
            item['followers'] = user.xpath('.//p[@class="userStats"]/span[@class="value"]/text()').extract()[1]
            items.append(item)

        return items
