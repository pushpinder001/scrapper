from enum import Enum

class ScrapperTarget(Enum):
	DENTALSTALL = (1, "https://dentalstall.com/shop/", 'page/{}/')

	def __init__(self, code, base_url, page_append_suffix):
		self.code = code
		self.base_url = base_url
		self.page_append_suffix = page_append_suffix