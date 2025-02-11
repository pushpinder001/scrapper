from dependency_injector import containers, providers
from app.controller.scrapper_controller import ScrapperController
from app.models.product_field_type import ProductFieldType
from app.models.scrapper_target import ScrapperTarget
from app.repository.file_product_repository import FileProductRepository 
from app.service.std_out_notification_service import StdOutNotificationService
from app.service.static_auth_service import StaticAuthService
from app.service.in_memory_cache_service import InMemoryCacheService
from app.service.dentalstall_scrapper_service import DentalStallScrapperService
from app.strategy.simple_retry_strategy import SimpleRetryStrategy
from app.strategy.product_price_parser_strategy import ProductPriceParserStrategy
from app.strategy.product_image_path_parser_strategy import ProductImagePathParserStrategy
from app.strategy.product_title_parser_strategy import ProductTitleParserStrategy
from app.strategy.product_html_tag_parser_strategy import ProductHtmlTagParserStrategy

import dataclasses
from typing import Dict

@dataclasses.dataclass
class Module:
    name: str

@dataclasses.dataclass
class Dispatcher:
    modules: Dict[str, Module]

# Dependency Injection Container
class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    product_parser_type_to_parser_mapping = {
      ProductFieldType.TITLE.name: ProductTitleParserStrategy(),
      ProductFieldType.PRICE.name: ProductPriceParserStrategy(),
      ProductFieldType.IMAGE_PATH.name: ProductImagePathParserStrategy()
    }

    # Bind interface to specific implementation
    product_repository = providers.Singleton(FileProductRepository)  # Default implementation
    notification_service = providers.Singleton(StdOutNotificationService)
    retry_strategy = providers.Singleton(SimpleRetryStrategy)
    cache_service = providers.Singleton(InMemoryCacheService)

    dentalstall_scrapper_service = providers.Singleton(DentalStallScrapperService, repository=product_repository, 
            notification_service=notification_service, retry_strategy=retry_strategy, 
            cache_service = cache_service,
            product_parser_type_to_parser_mapping = product_parser_type_to_parser_mapping)

    dispatcher_factory = providers.Factory(
        dict,
        modules = providers.Dict({
                ScrapperTarget.DENTALSTALL.name : providers.Factory(dentalstall_scrapper_service)
            }
        ),
    )

    scrapper_controller = providers.Singleton(ScrapperController, dispatcher_factory)
    auth_service = providers.Singleton(StaticAuthService)