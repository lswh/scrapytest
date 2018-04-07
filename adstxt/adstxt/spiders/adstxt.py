import scrapy


class AdstxtSpider(scrapy.Spider):
    name = "adstxt"
    def  start_requests(self):

        urls=[]
        with open("xfm") as file:
            for line in file: 
                line = line.strip()
                urls.append('http://'+line+'/ads.txt') 

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
