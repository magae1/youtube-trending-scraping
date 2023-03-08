import os

from scrapy.spiderloader import SpiderLoader
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


# 'AWS_EXECUTION_ENV'는 예약어(reserved word)
# https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html
def is_in_aws():
    return os.getenv('AWS_EXECUTION_ENV') is not None


def crawl(settings={}, spider_name="youtube", spider_kwargs={}):
    project_settings = get_project_settings()
    spider_loader = SpiderLoader(project_settings)

    spider_cls = spider_loader.load(spider_name)

    if is_in_aws():
        feed_uri = 'file:///tmp/1.'
    else:
        feed_uri = "1."

    feed_format = "xml"
    feed_uri += feed_format

    settings['FEED_URI'] = feed_uri
    settings['FEED_FORMAT'] = feed_format

    process = CrawlerProcess({**project_settings, **settings})

    process.crawl(spider_cls, **spider_kwargs)
    process.start()
