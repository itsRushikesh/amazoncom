import scrapy


class AmazonSpider(scrapy.Spider):
    name = "amazon"
    # allowed_domains = ["www.xx.com"]
    start_urls = ["https://www.amazon.in/gp/bestsellers/luggage/ref=bs_luggage_sm"]

    def parse(self, response):
        products = response.xpath("//div[@class='p13n-sc-uncoverable-faceout']/a[@tabindex='-1']/@href").getall()
        
        for links in products:
            yield response.follow(links, callback = self.parse2)
        
    
    def parse2(self, response):
        pass
        product_name = response.xpath("//span[@id = 'productTitle']/text()").get()
        price = response.xpath("//span[@class = 'a-price-whole']/text()").get()
        availability = response.xpath("//div[@id = 'availability']/span/text()").get()
        
        yield{
            'product':product_name,
            'prices': price,
            'availability': availability
        }
        
        
