# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CarUsagePipeline(object):

    def process_item(self, item, spider):
        is_new = str(item["is_new"])

        if ("Used" in is_new):
            item["is_new"] = 0
        else:
            item["is_new"] = 1
        return item
