import scrapy


class AdstxtSpider(scrapy.Spider):
    name = "adstxt"

    def start_requests(self):
        #Initialize empty array urls for URL listing from the domains to be tested. 
        urls = []
        
        # Get the file containing the URLs from Alexa's top 1 million list or other data source. 

        #Open the file and load as pandas dataframe?

        #For loop that each line containing the URL will be appended as a list item in urls



        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)