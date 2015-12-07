from scrapy.exceptions import DropItem


class FilterAccountsPipeline(object):
    
    def process_item(self, item, spider):
        if item ['followers']:
            try int(item['followers']):
                return item
            except ValueError:
                raise DropItem('To Many Followers")
        else:
            raise DropItem("No Item found")
