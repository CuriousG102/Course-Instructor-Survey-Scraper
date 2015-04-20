# -*- coding: utf-8 -*-
import urlparse

import scrapy

from scrapy.http import FormRequest, Request
from scrapy.selector import Selector

from w3lib.url import url_query_cleaner

from ..items import CISItem

class PublicCISSpider(scrapy.Spider):
    name = "publicCIS"
    allowed_domains = ["utexas.edu"]
    start_urls = (
        'http://utdirect.utexas.edu/ctl/ecis/results/index.WBX',
    )

    def parse(self, response):
        for num in xrange(65, 91):
            yield FormRequest.from_response(response, 
                                            formdata={'s_in_search_name':chr(num)},
                                            clickdata={'value':'Search'},
                                            callback = self.resultsPage)

    def resultsPage(self, response):
        table = response.selector.xpath('/html/body/div/div[3]/div[2]/table')
        cisResultLinks = table.css('.left-align').xpath('a/@href').extract()
        for link in cisResultLinks:
            yield Request(urlparse.urljoin(response.url, link), 
                          callback = self.surveyResult)

        if len(response.selector.xpath('//input[@value="Next page"]')) != 0:
            yield FormRequest.from_response(response,
                                            formxpath='//div[@class="page-forward"]/form[1]',
                                            url = url_query_cleaner(response.url), # workaround for scrapy problem
                                            callback = self.resultsPage)

    def surveyResult(self, response):
        i = CISItem()

        details = response.selector.css('.details-box').xpath('div/text()[last()]').extract()
        i['instructor'] = details[0]
        i['course_and_unique_num'] = details[1]
        i['organization'] = details[2]
        i['college_school'] = details[3]
        i['semester'] = details[4]
        i['forms_distributed'] = details[5]
        i['forms_returned'] = details[6]

        table = response.selector.xpath('//table')
        secondRow = table.xpath('tr[2]')
        thirdRow = table.xpath('tr[3]')

        criteria = ('_was_num_respondents', '_was_average', '_was_org_average',
                    '_was_college_school_average', '_was_uni_average')

        for j, criterion in enumerate(criteria):
            i['instructor%s' % criterion] = secondRow.xpath('td[%d]/text()' % (j + 2)).extract()[0]
            i['course%s' % criterion] = thirdRow.xpath('td[%d]/text()' % (j + 2)).extract()[0]

        return i








