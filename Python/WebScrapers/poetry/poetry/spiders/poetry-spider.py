import scrapy

class PoetrySpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
                'http://shakespeare.mit.edu/allswell/full.html'
                ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'{page}.txt'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
