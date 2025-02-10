from app.models.dto.scrape_request import ScrapeRequestDTO
from app.models.product_field_type import ProductFieldType
from app.repository.file_product_repository import FileProductRepository
from app.repository.file_product_repository import ProductRepositoryInterface
from app.strategy.retry_strategy import RetryStrategy
from app.service.scrapper_service_interface import ScrapperServiceInterface
from app.service.cache_service_interface import CacheServiceInterface
from app.service.notification_service_interface import NotificationServiceInterface
import logging
import os
import requests
from bs4 import BeautifulSoup
import json

class ScrapperService(ScrapperServiceInterface):
    """
    Service class that handles the business logic for scrapping.
    """
    def __init__(self, repository: ProductRepositoryInterface, 
            notification_service: NotificationServiceInterface,
            retry_strategy: RetryStrategy, 
            cache_service: CacheServiceInterface,
            product_parser_type_to_parser_mapping):
        self.repository = repository
        self.notification_service = notification_service
        self.retry_strategy = retry_strategy
        self.cache_service = cache_service
        self.product_parser_type_to_parser_mapping = product_parser_type_to_parser_mapping
        self.LOGGER = logging.getLogger(__name__)
        
    def run(self, scrape_request: ScrapeRequestDTO, scrapper_target) -> dict:
        self.LOGGER.info("Entered scrapper service" + str(scrapper_target))
        """Scrape product details from the website."""

        page_urls = self.get_page_urls(scrape_request.meta_data.num_pages, scrapper_target)

        # Updated products counts
        updated_products_cnt=0

        for page_url in page_urls:
            self.LOGGER.info("Page Url " + str(page_url))
            product_feild_strs = scrape_request.meta_data.field_name
            
            product_feilds = []
            for prod_field in product_feild_strs:
                product_feilds.append(ProductFieldType[prod_field])

            try:
                response = self.retry_strategy.make_request("GET", page_url)

                self.LOGGER.info("Got response " + str(response))
                response.raise_for_status()
                soup = BeautifulSoup(response.content, "html.parser")

                # Find all product cards
                product_cards = soup.find_all("li", class_="product")
                self.LOGGER.info("Current page has " + str(len(product_cards)) + " products")

                for card in product_cards:
                    try:
                        product = {}
                        for product_feild in product_feilds:
                            if(product_feild.name in self.product_parser_type_to_parser_mapping) : 
                                value = self.product_parser_type_to_parser_mapping[product_feild.name].parse(card)
                                product[product_feild.field_name] = value

                        product_title = product[ProductFieldType.TITLE.field_name]
                        saved_product = self._get_product_by_title(product_title)

                        if(saved_product is None or product[ProductFieldType.PRICE.field_name] != 
                                saved_product[ProductFieldType.PRICE.field_name]):
                            # Update product data
                            updated_products_cnt+=1
                            self.repository.save_product(product)
                            self.cache_service.put(product_title, product)
                            self.LOGGER.info("Updated product " + str(product_title))
                    except Exception as e:
                        self.LOGGER.error("Error processing a product card: " + str(e))

            except Exception as e:
                self.LOGGER.error("Failed to scrape the website: " + str(e))
            self.LOGGER.info("Scraping completed. " + str(updated_products_cnt) + " products updated in product storage")
            self.notification_service.notify("Scraping completed. " + str(updated_products_cnt) +  " products updated in product storage")

    def get_page_urls(self, no_of_pages, scrapper_target):
        page_urls = []
        base_url = scrapper_target.base_url
        page_append_suffix = scrapper_target.page_append_suffix
        for i in range(1, no_of_pages+1):
            url = base_url +  page_append_suffix.format(i)
            page_urls.append(url)

        return page_urls

    def _get_product_by_title(self, product_title):
        val = self.cache_service.get(product_title)
        if(val is None):
            val = self.repository.get_product_by_name(product_title)
            if(val is not None):
                self.cache_service.put(product_title, val)
        return val

