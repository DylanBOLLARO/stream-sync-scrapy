import scrapy
from stream_sync_scrapy.items import MovieItem


class QuotesSpider(scrapy.Spider):
    name = "allocine"
    allowed_domains = ["allocine.fr"]
    base_url = "https://www.allocine.fr/film/meilleurs/decennie-2020"

    def start_requests(self):
        page_to_scrape = 2
        index = 0

        while index < page_to_scrape:
            index += 1
            yield scrapy.Request(
                url=self.base_url + ("/?page=" + str(index) if index > 1 else ""),
                callback=self.parse,
            )

    def parse(self, response):
        print(response.url)

        for movie_selector in response.xpath("//li[@class='mdl']"):
            item = MovieItem()

            # title
            title = movie_selector.xpath('.//h2[@class="meta-title"]/a/text()').get()
            item["title"] = title if title else None

            # url
            url = movie_selector.xpath('.//h2[@class="meta-title"]/a/@href').get()
            item["url"] = "https://www.allocine.fr" + url if url else None

            # synopsis
            synopsis = movie_selector.xpath(
                './/div[@class="synopsis"]/div/text()'
            ).get()
            item["synopsis"] = synopsis.strip() if synopsis else None

            # duration
            duration = movie_selector.xpath(
                './/div[@class="meta-body-item meta-body-info"]/text()'
            ).re_first(r"(\d+h \d+min)")
            item["duration"] = duration if duration else None

            # genres
            genres = movie_selector.xpath(
                './/div[@class="meta-body-item meta-body-info"]/span[@clas="dark-grey-link"]/text()'
            ).getall()
            item["genres"] = genres if genres else None

            # directors
            directors = movie_selector.xpath(
                '//div[@class="meta-body-item meta-body-direction "]/span/text()'
            ).getall()
            item["directors"] = (
                [director for director in directors if director.lower() != "de"]
                if directors
                else None
            )

            # actors
            actors = movie_selector.xpath(
                '//div[@class="meta-body-item meta-body-actor"]/a/text()'
            ).getall()
            item["actors"] = actors if actors else None

            # audience_rating
            audience_rating = movie_selector.xpath(
                './/div[contains(@class, "rating-item")]'
                '[.//a[contains(text(), "Spectateurs")]]'
                '//span[@class="stareval-note"]/text()'
            ).get()
            item["audience_rating"] = audience_rating if audience_rating else None

            yield scrapy.Request(
                url="https://www.allocine.fr" + url,
                callback=self.depth_parse,
                meta={"item": item},
            )

    def depth_parse(self, response):
        print("depth_parse called for URL:", response.url)
        item = response.meta.get("item")
        image_url = response.xpath(
            '//div[@class="card entity-card entity-card-list cf entity-card-player-ovw"]//img[@class="thumbnail-img"]/@src'
        ).get()
        item["image_urls"] = [image_url] if image_url else None
        yield item
