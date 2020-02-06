# -*- coding: utf-8 -*-
import scrapy


class SamsungMobilesSpider(scrapy.Spider):
    name = 'samsung_mobiles'
    allowed_domains = ['www.flipkart.com/samsung-mobile-store?otracker=nmenu_sub_Electronics_0_Samsung']
    start_urls = ['http://www.flipkart.com/samsung-mobile-store?otracker=nmenu_sub_Electronics_0_Samsung/']
    #locations for the csv files
    custom_settings = {
    	"FEED_URI": "tmp/samsung_mobiles.csv"
    }

    def parse(self, response):
        name = response.css("._2cLu-l::text").extract()
        rating = response.css(".hGSR34::text").extract()
        price = response.css("._1vC4OE::text").extract()
        img = response.css("._3BTv9X img::attr(src)").extract()

        for item in zip(name, rating, price, img):
        	scraped_info = {
        		"Mobile Name": item[0],
        		"User Rating": item[1],
        		"price": item[2],
        		"image_url": [item[3]]
        	}

        	yield scraped_info
