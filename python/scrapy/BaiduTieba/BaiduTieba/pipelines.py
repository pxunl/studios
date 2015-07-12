# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import urllib
import os
import time
from BaiduTieba import settings
import random

class BaidutiebaPipeline(object):
    def process_item(self, item, spider):
		_file_path = settings.IMAGE_STORE
		print "==============Begin crawls===============\n"
		if not os.path.exists(_file_path):
			os.mkdir(_file_path)
		if not item:
			return
		#print item
		#for it in item:
		try:
			current_time = time.strftime('%H:%M:%S')
			heights = item.get('height')
			widths = item.get('width')
			links = item.get('link')
			pic_types = item.get('pictype')
			for i, link in enumerate(links):
				#pic_type = pic_types[i]
				if not link or not link.endswith('.jpg'):
					continue
				print '\ndownloading',link
				img = '%s/%s-%s-%s' % (_file_path, str(i), str(current_time), str(random.uniform(1,
					100)))
				if os.path.exists(img):
					continue
				urllib.urlretrieve(link, img)
		except:
			print 'Download Error'
