import re
from scrapy.pipelines.images import ImagesPipeline


class MyImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        normalized_text = re.sub(r"[^a-zA-Z0-9]+", "-", item["title"])
        normalized_text = normalized_text.strip("-")
        normalized_text = normalized_text.lower()
        return f"{normalized_text}.jpg"
