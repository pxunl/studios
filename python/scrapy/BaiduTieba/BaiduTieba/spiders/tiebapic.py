import scrapy
from BaiduTieba.items import Item
import os
class TiebaPic(scrapy.Spider):
	name = "tiebapic"
	allowed_domains = ["baidu.com"]
	start_urls = [
			]

	def parse(self, response):
            '''Version 1'''
            #sel = scrapy.Selector(respone)
            #for l in sel.xpath('//img[@class="BDE_Image" and @pic_ext]'):
            #for l in sel.xpath('//div/"d_post_content j_d_post_content "img[@class="BDE_Image" and @pic_ext]'):
                #item =Item()
                #item['link'] = l.xpath('//@src').extract()
                #item['height'] = lr.xpath('//@height').extract()
                #item['width'] = l.xpath('//@width').extract()
                #item['pictype'] = l.xpath('//@pic_type').extract()
                #items.append(item)
            #yield

            '''version 2 get base urls'''
            hrefs = response.xpath('//a[contains(@target, "_blank") and contains(@class, "j_th_tit")]/@href').extract()
            targets = len(hrefs)
            print "\nAll targets", hrefs
            print '\nTarget num [%d]' % targets

            base_url = scrapy.utils.response.get_base_url(response)
            print '\nBaseurl:', base_url
            urls = [scrapy.utils.url.urljoin_rfc(base_url, href) for href in hrefs]
            print '\nRelativeurl:', urls
            requests = [scrapy.Request(url, callback = self.parse_item) for url in urls]
            return requests
            #item['link'] = respone.xpath('//img[contains(@class, "BDE_Image")]/@src').extract()
            #return item

        def parse_item(self, response):
            item =Item()
            item['link'] = response.xpath('//img[contains(@class, "BDE_Image")]/@src').extract()
            item['title'] = response.xpath('//img[contains(@class, "BDE_Image")]/@src').extract()
            return item

