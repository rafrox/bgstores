from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class Milspider(BasePortiaSpider):
    name = "Milspider"
    allowed_domains = [u'www.milsims.com.au']
    start_urls = [u'http://www.milsims.com.au/catalog/1746',
                  {u'url': u'http://www.milsims.com.au/catalog/1746?page=[1-9]',
                   u'fragments': [{u'valid': True,
                                   u'type': u'fixed',
                                   u'value': u'http://www.milsims.com.au/catalog/1746?page='},
                                  {u'valid': True,
                                   u'type': u'range',
                                   u'value': u'1-9'}],
                   u'type': u'generated'}]
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.views-view-grid > tr > td, .views-view-grid > tbody > tr > td',
                [
                    Field(
                        u'Title',
                        '.views-field-field-image-cache-fid > .field-content > .imagecache > .imagecache::attr(title)',
                        []),
                    Field(
                        u'Img_src',
                        '.views-field-field-image-cache-fid > .field-content > .imagecache > .imagecache::attr(src)',
                        []),
                    Field(
                        u'Price',
                        '.views-field-phpcode > .field-content > span:nth-child(2) *::text',
                        [])])]]
