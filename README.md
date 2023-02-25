# 유튜브 실시간 인기 동영상 스크래핑(Youtube trending scraping) with Dockerfile


* This project is for practice of scrapy-playwright.
* Browser for scraping runs on 'ko-kr'(KOREAN.ver)

How to build docker
===============

    > docker build . -t [image-name]

Example
===============
**- request**

    > curl -v "http://localhost:9080/crawl.json?spider_name=youtube&start_requests=true"

**- response**

    {
        "status": "ok",
        "items": [
                    {
                        "rank": 1,
                        "title": "..",
                        "url": "watch?v=..",
                        "views": "123456", 
                        "channel": "channel-name", 
                        "handle": "@channel-handle"}, 
                    {
                        "rank": 2,
                        "title: ".."
                    },
                    ...
                ], 
        "items_dropped": [], 
        "stats": {
                    "downloader/request_bytes": 670,
                    "downloader/request_count": 3,
                    "downloader/request_method_count/GET": 3,
                    "downloader/response_bytes": 3611845,
                    "downloader/response_count": 3,
                    "downloader/response_status_count/200": 2,
                    "downloader/response_status_count/301": 1,
                    "elapsed_time_seconds": 17.74578,
                    "finish_reason": "finished",
                    "finish_time": "2023-02-25 10:37:32",
                    "httpcompression/response_bytes": 662,
                    "httpcompression/response_count": 1, 
                    "item_scraped_count": 50, 
                    "log_count/DEBUG": 148, 
                    "log_count/INFO": 19, 
                    "memusage/max": 132218880, 
                    "memusage/startup": 132218880, 
                    "playwright/context_count": 2,      
                    "playwright/context_count/max_concurrent": 1, 
                    "playwright/context_count/non_persistent": 2, 
                    "playwright/page_count": 1, 
                    "playwright/page_count/closed": 1, 
                    "playwright/page_count/max_concurrent": 1, 
                    "playwright/request_count": 46, 
                    "playwright/request_count/method/GET": 45, 
                    "playwright/request_count/method/POST": 1, 
                    "playwright/request_count/navigation": 4, 
                    "playwright/request_count/resource_type/document": 4, 
                    "playwright/request_count/resource_type/fetch": 2, 
                    "playwright/request_count/resource_type/font": 3, 
                    "playwright/request_count/resource_type/image": 13, 
                    "playwright/request_count/resource_type/media": 4, 
                    "playwright/request_count/resource_type/script": 10, 
                    "playwright/request_count/resource_type/stylesheet": 7, 
                    "playwright/request_count/resource_type/xhr": 3, 
                    "playwright/response_count": 46, 
                    "playwright/response_count/method/GET": 45, 
                    "playwright/response_count/method/POST": 1, 
                    "playwright/response_count/resource_type/document": 4, 
                    "playwright/response_count/resource_type/fetch": 2, 
                    "playwright/response_count/resource_type/font": 3, 
                    "playwright/response_count/resource_type/image": 13, 
                    "playwright/response_count/resource_type/media": 4, 
                    "playwright/response_count/resource_type/script": 10, 
                    "playwright/response_count/resource_type/stylesheet": 7, 
                    "playwright/response_count/resource_type/xhr": 3, 
                    "response_received_count": 2, 
                    "robotstxt/request_count": 1, 
                    "robotstxt/response_count": 1, 
                    "robotstxt/response_status_count/200": 1,
                    "scheduler/dequeued": 1, 
                    "scheduler/dequeued/memory": 1, 
                    "scheduler/enqueued": 1, 
                    "scheduler/enqueued/memory": 1, 
                    "start_time": "2023-02-25 10:37:15"
              }, 
          "spider_name": "youtube"
      }