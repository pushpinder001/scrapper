from app.strategy.product_html_tag_parser_strategy import ProductHtmlTagParserStrategy
import logging

class ProductTitleParserStrategy(ProductHtmlTagParserStrategy):
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)

    def parse(self, card) :
        add_to_cart_link = card.select_one('.footer-button .addtocart-buynow-btn a[data-title]')

        title = add_to_cart_link.get('data-title') if add_to_cart_link else "Unknown Title"
        return title