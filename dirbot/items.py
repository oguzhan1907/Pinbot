from scrapy.item import Item, Field


class Website(Item):

    usr_name = Field()
    pins = Field()
    followers = Field()
