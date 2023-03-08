import os
import json
import sys
import xmltodict as xd
from youtube_scrapy.crawl import is_in_aws, crawl


def handler(event={}, context={}):
    crawl(**event)

    if is_in_aws():
        file_name = "file:///tmp/1.xml"
    else:
        file_name = "1.xml"
    with open(file_name, 'r') as file:
        results = json.dumps(xd.parse(file.read()), indent=4)

    os.remove(file_name)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": results
    }


if __name__ == "__main__":
    try:
        event = json.loads(sys.argv[1])
    except IndexError:
        event = {}
    handler(event)
