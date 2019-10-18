from scrapy import Request
from scrapy.spiders import Spider

class ItunesSpider(Spider):
    name = "itunes"
    handle_httpstatus_list = [404, 403]
    allowed_domains = ["apple.com"]
    start_urls = ["https://www.apple.com/uk/itunes/charts/free-apps/"]
    custom_settings = {'DOWNLOAD_DELAY': 0.5}

    def parse(self, response):
        apps = response.xpath("//div[@class='main']/section[@class='section apps chart-grid']\
        /div[@class='section-content']/ul/li")
        ans=[]
        for app in apps:
            item = {}
            item['app_name'] = app.xpath('./h3/a/text()').extract()
            item['category'] = app.xpath('./h4/a/text()').extract()
            item['appstore_link_url'] = app.xpath('./a/@href')[0].extract()
            item['img_src_url'] = app.xpath('./a/img/@src').extract()
            url = item['appstore_link_url']
            req = Request(url, callback = self.parse_2)
            # hashtable, share information between request and response
            req.meta['foo'] = item
            ans.append(req)            
        return ans

    def parse_2(self, response):
        item = response.meta['foo']
        item['star_rating'] = response.xpath("//div[@class='l-row']\
                /div[@class='we-customer-ratings__stats l-column small-4 medium-6 large-4']\
                /div[@class='we-customer-ratings__averages']\
                /span[@class='we-customer-ratings__averages__display']/text()").extract()
        item['number_rating'] = response.xpath("//div[@class='l-row']\
                /div[@class='we-customer-ratings__stats l-column small-4 medium-6 large-4']\
                /div[@class='we-customer-ratings__count small-hide medium-show']/text()").extract()
        return item