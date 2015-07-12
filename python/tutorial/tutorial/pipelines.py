# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import urllib
from tutorial import settings
import os

class TutorialPipeline(object):
    def process_item(self, item, spider):
		images = []
		#dir_path = '%s/%s' %(settings.IMAGE_STORE, tiebas)
		dir_path = './teibas'


		print 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'*100
		#if not os.path.exists(dir_path):
		os.mkdir("./cc")

        n = 0
		for i in item:
			url = i['link']
			file_path = '%s/%s' % (dir_path, str(n))
			n += 1
			if os.path.exists(file_path):
				continue
			images.append(file_path)
			urllib.urlretrieve(url, str(n) + '.jgp')
			print 'Download %s done' % (str(n) + '.jpg')
		item['images'] = images
        return item
