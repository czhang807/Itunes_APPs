from scrapy import Request
from scrapy.spiders import Spider

class S1(Spider):
    name = 's1'
    #allowed_domains
    start_urls = ["https://apps.apple.com/gb/app/whatsapp-messenger\
    /id310633997?v0=WWW-EUUK-ITSTOP100-FREEAPPS&l=en&ign-mpt=uo%3D4"]

    def parse(self, response):
        ans={}
        ans['star_rating'] = response.xpath("//div[@class='l-row']\
        /div[@class='we-customer-ratings__stats l-column small-4 medium-6 large-4']\
        /div[@class='we-customer-ratings__averages']\
        /span[@class='we-customer-ratings__averages__display']/text()").extract()
        ans['number_rating'] = response.xpath("//div[@class='l-row']\
        /div[@class='we-customer-ratings__stats l-column small-4 medium-6 large-4']\
        /div[@class='we-customer-ratings__count small-hide medium-show']/text()").extract()
        return ans
