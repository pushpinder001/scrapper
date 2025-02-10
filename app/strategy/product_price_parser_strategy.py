from app.strategy.product_html_tag_parser_strategy import ProductHtmlTagParserStrategy
import logging

class ProductPriceParserStrategy(ProductHtmlTagParserStrategy):
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)

    def parse(self, card) :
        price_tag = card.find("span", class_="woocommerce-Price-amount")
        price = price_tag.text.strip()[1:] if price_tag else "Unknown Price"
        return price