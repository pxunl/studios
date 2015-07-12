import scrapy
from tutorial.items import Item
import os
import urllib
class DmozSpider(scrapy.Spider):
	name = "dmoz"
	allowed_domains = ["baidu.com"]
	start_urls = [
			#"http://tieba.baidu.com/f?kw=%E4%B8%9D%E8%A2%9C&ie=utf-8",
            "http://tieba.baidu.com/p/3873147363?fr=frs"
			]

	def parse(self, respone):
		sel = scrapy.Selector(respone)
		items = []
		n = 0
		for l in sel.xpath("//img[@class='BDE_Image']"):
			item =Item()
			item['link'] = l.xpath('//@src').extract()
			item['height'] = l.xpath('//@height').extract()
			item['width'] = l.xpath('//@width').extract()
			item['pic_ext'] = l.xpath('//@pic_ext').extract()
			items.append(item)
			#print filen,'ccccccccccccccccccccc\n',item['link']
			for i in item['link']:
				filen =  str(n) + '.jgp'
				print '...........' , i, filen, '\n'
				urllib.urlretrieve(i, filen)
				n += 1
			return items
