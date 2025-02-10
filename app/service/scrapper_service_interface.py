from abc import ABC, ABCMeta, abstractmethod
from app.models.dto.scrape_request import ScrapeRequestDTO

# Repository interface
class ScrapperServiceInterface(ABC):
    @abstractmethod
    def run(self, scrape_request: ScrapeRequestDTO, scrapper_target):
        pass        