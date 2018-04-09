# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
class MySpider(CrawlSpider):
    name = "advent"
    allowed_domains = ["www.adventgames.com.au/"]
    start_urls = [u'http://www.adventgames.com.au/c/4504822/1/all-games-a---k.html',
                  {u'url': u'http://www.adventgames.com.au/Listing/Category/?categoryId=4504822&page=[1-5]',
                   u'fragments': [{u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'http://www.adventgames.com.au/Listing/Category/?categoryId=4504822&page='},
                                  {u'valid': True,
                                   u'type': u'range',
                                   u'value': u'1-5'}],
                   u'type': u'generated'}]

    def __init__(self, *a, **kw):
        super(MySpider, self).__init__(*a, **kw)
        dispatcher.connect(self.spider_closed, signals.spider_closed)
