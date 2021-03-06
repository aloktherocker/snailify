# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinglescrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class PersonProfileItem(Item):
    id = Field()
    name_linkedin = Field()
    title = Field()
    location = Field()
    industry = Field()
    current_company = Field()
    past_company = Field()
    education = Field()
    url = Field()
    summary = Field()
    connection = Field()
    email = Field()
    image = Field()
    experience = Field()
    birthday = Field()
    phone = Field()
