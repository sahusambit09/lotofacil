# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LotofacilItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    ticket_numbers = scrapy.Field()
    contestNo = scrapy.Field()
    entryDate = scrapy.Field()
    est_next_contest = scrapy.Field()
    five_final_contest = scrapy.Field()
    jackpot_mega_draw = scrapy.Field()
    next_contest_prize = scrapy.Field()
    created_date = scrapy.Field()
