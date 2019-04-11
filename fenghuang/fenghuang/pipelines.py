# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FenghuangPipeline(object):
    def process_item(self, item, spider):
        # print(item['title'],item['link'],item['biaoti'],item['biaotilianjie'])
        with open('index.txt','a',encoding="utf8") as f:
            # f.write("%s %s"%(item['title'],item['link']))
            # f.write("\n")
            f.write("%s %s %s %s %s %s"%(item['title'],item['link'],item['biaoti'],item['biaotilianjie'],item['time'],item['neirong']))
            f.write("\n")
        return item
