import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
        'http://macrumors.com/ads.txt',
        'http://google.com/ads.txt',
        'http://youtube.com/ads.txt',
        'http://wikipedia.org/ads.txt',
        'http://yahoo.com/ads.txt',
        'http://reddit.com/ads.txt',
        'http://google.co.in/ads.txt',
        'http://qq.com/ads.txt',
        'http://taobao.com/ads.txt',
        'http://tmall.com/ads.txt',
        'http://twitter.com/ads.txt',
        'http://amazon.com/ads.txt',
        'http://instagram.com/ads.txt',
        'http://live.com/ads.txt',
        'http://google.co.jp/ads.txt',
        'http://sohu.com/ads.txt',
        'http://vk.com/ads.txt',
        'http://sina.com.cn/ads.txt',
        'http://jd.com/ads.txt',
        'http://weibo.com/ads.txt',
        'http://360.cn/ads.txt',
        'http://google.de/ads.txt',
        'http://google.co.uk/ads.txt',
        'http://google.com.br/ads.txt',
        'http://yandex.ru/ads.txt',
        'http://google.fr/ads.txt',
        'http://login.tmall.com/ads.txt',
        'http://google.ru/ads.txt',
        'https://linkedin.com/ads.txt',           
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)