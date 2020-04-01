# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_id = scrapy.Field()
    hebrew_name = scrapy.Field()
    company_type = scrapy.Field()
    company_status = scrapy.Field()
    company_status2 = scrapy.Field()
    company_last_year_report = scrapy.Field()

    english_name = scrapy.Field()
    company_start_date = scrapy.Field()
    company_desc = scrapy.Field()
    company_desc_2 = scrapy.Field()
    company_limit = scrapy.Field()
    company_task = scrapy.Field()
    company_address = scrapy.Field()
    company_info = scrapy.Field()
