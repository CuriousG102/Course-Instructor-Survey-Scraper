# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CISItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    instructor = scrapy.Field()
    course_and_unique_num = scrapy.Field()
    organization = scrapy.Field()
    college_school = scrapy.Field()
    semester = scrapy.Field()
    forms_distributed = scrapy.Field()
    forms_returned = scrapy.Field()
    instructor_was_num_respondents = scrapy.Field()
    instructor_was_average = scrapy.Field()
    instructor_was_org_average = scrapy.Field()
    intructor_was_college_school_average = scrapy.Field()
    instructor_was_uni_average = scrapy.Field()
    course_was_num_respondents = scrapy.Field()
    course_was_average = scrapy.Field()
    course_was_org_average = scrapy.Field()
    course_was_college_school_average = scrapy.Field()
    course_was_uni_average = scrapy.Field()