import scrapy


class VideoItem(scrapy.Item):
    rank = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    views = scrapy.Field()
    channel = scrapy.Field()
    handle = scrapy.Field()
