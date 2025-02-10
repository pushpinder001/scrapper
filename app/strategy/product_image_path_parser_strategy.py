from app.strategy.product_html_tag_parser_strategy import ProductHtmlTagParserStrategy
import logging

class ProductImagePathParserStrategy(ProductHtmlTagParserStrategy):
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)

    def parse(self, card) :
        image_tag = card.find("img", class_="attachment-woocommerce_thumbnail")
        image_url = image_tag["data-lazy-src"] if image_tag and "data-lazy-src" in image_tag.attrs else None
        return image_url