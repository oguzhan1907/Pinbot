import json
from scrapy.exceptions import DropItem



class FilterAccountsPipeline(object):
    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        if item ['followers']:
            try:
                item['followers'] *= 1
                line = json.dumps(dict(item)) + "\n"
                self.file.write(line)
                return item
            except TypeError:
                raise DropItem('To Many Followers')





