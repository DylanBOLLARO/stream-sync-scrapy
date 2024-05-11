import scrapy


class MovieItem(scrapy.Item):
    title = scrapy.Field()
    duration = scrapy.Field()
    genres = scrapy.Field()
    directors = scrapy.Field()
    actors = scrapy.Field()
    original_title = scrapy.Field()
    age_rating = scrapy.Field()
    press_rating = scrapy.Field()
    audience_rating = scrapy.Field()
    synopsis = scrapy.Field()
    streaming_link = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    url = scrapy.Field()
