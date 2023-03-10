from pathlib import Path

import scrapy


class GithubSpider(scrapy.Spider):
    name = "github"

    def start_requests(self):
        # go through e
        urls = [
            'https://github.com/search?',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')