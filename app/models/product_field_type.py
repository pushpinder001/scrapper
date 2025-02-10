from enum import Enum

class ProductFieldType(Enum):
	TITLE = (1, "product_title")
	PRICE = (2, "product_price")
	IMAGE_PATH = (3, "path_image_path")

	def __init__(self, code, field_name):
		self.code = code
		self.field_name = field_name