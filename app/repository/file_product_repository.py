import json
import logging
from app.models.product_field_type import ProductFieldType
from app.repository.product_repository_interface import ProductRepositoryInterface

class FileProductRepository(ProductRepositoryInterface):
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)
        self.products = {}
        items = self.get_products()

        for item in items:
            self.products[item[ProductFieldType.TITLE.field_name]] = item

    def save_product(self, product) -> None:
        self.products[product[ProductFieldType.TITLE.field_name]] = product

        # Save the data to a JSON file
        with open("products.json", "w") as json_file:
            #for p in list(self.products.values()):
            json.dump(list(self.products.values()), json_file, indent=4)

    def get_products(self):
        try:
            with open("products.json", 'r+') as file:
                data = json.load(file)
                return data
        except:
            self.LOGGER.error("Unable to read file product.json data")
        return []

    def get_product_by_name(self, product_name):
        val = self.products.get(product_name)
        return val