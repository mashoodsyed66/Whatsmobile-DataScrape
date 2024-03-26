# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WhatmobileItem(scrapy.Item):
    name = scrapy.Field()
    os = scrapy.Field()
    weight = scrapy.Field()
    sim = scrapy.Field()
    band_4g = scrapy.Field()
    cpu = scrapy.Field()
    chipset = scrapy.Field()
    gpu = scrapy.Field()
    display_technology = scrapy.Field()
    display_size = scrapy.Field()
    display_resolution = scrapy.Field()
    display_extra_features = scrapy.Field()
    memory_built_in = scrapy.Field()
    card = scrapy.Field()
    camera_main = scrapy.Field()
    camera_features = scrapy.Field()
    camera_front = scrapy.Field()
    wlan = scrapy.Field()
    gps = scrapy.Field()
    data = scrapy.Field()
    sensors = scrapy.Field()
    extra_features = scrapy.Field()
    battery_capacity = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()