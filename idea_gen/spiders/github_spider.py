from pathlib import Path

import scrapy


class GithubSpider(scrapy.Spider):
    name = "github"

    def start_requests(self):
        # go through each search query for ideas
        urls = [
            'https://github.com/search?',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #get all links from search results
        # response.css('.repo-list-item .v-align-middle::attr(href)').getall()

        
        
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')