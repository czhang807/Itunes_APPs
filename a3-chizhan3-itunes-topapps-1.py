
from scrapy import Request
from scrapy.spiders import Spider

class S1(Spider):
    name = 's1'
    #allowed_domains
    start_urls = ["https://www.apple.com/uk/itunes/charts/free-apps/"]

    def parse(self, response):
        apps = response.xpath("//div[@id='main']\
        /section[@class='section apps chart-grid']/div[@class='section-content']/ul/li")
        ans=[]
        for app in apps:
            item = {}
            item['app_name'] = app.xpath('./h3/a/text()').extract()
            item['category'] = app.xpath('./h4/a/text()').extract()
            item['appstore_link_url'] = app.xpath('./a/@href')[0].extract()
            item['img_src_url'] = app.xpath('./a/img/@src').extract()
            ans.append(item)
        return ans
