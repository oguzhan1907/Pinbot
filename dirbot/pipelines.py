import json
from scrapy.exceptions import DropItem


class FilterAccountsPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        if "k" in item['followers']:
           raise DropItem('To Many Followers')
        else:
            line = json.dumps(dict(item)) + "\n"
            self.file.write(line)
            return item
