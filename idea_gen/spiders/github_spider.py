from pathlib import Path

import scrapy


class GithubSpider(scrapy.Spider):
    name = "github"

    def start_requests(self):
        # go through each search query for ideas
        urls = [
            'https://github.com/search?q={}'.format("project+ideas"),
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #get all links from search results
        # 
        for link in response.css('.repo-list-item .v-align-middle::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_repo)
    
    def parse_repo(self, response):
        markdown = response.css('.markdown-body')
        for element in markdown:
            yield {
                'h1': element.css('h1::text').get().strip(),
                'h3': element.css('h2::text').getall(),
            }
            for li in element.css('li::text').getall():
                yield {
                    li.strip()
                }