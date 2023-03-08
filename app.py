import os
from youtube_scrapy.crawl import is_in_aws, crawl


def handler(event, context={}):
    crawl(**event)

    if is_in_aws():
        file_name = "file:///tmp/1.json"
    else:
        file_name = "1.json"
    with open(file_name, 'r') as file:
        results = file.read()

    os.remove(file_name)

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": results
    }


# if __name__ == "__main__":
#     try:
#         event = json.loads(sys.argv[1])
#     except IndexError:
#         event = {}
#     print(handler(event))

