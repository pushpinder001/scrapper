from abc import ABC, ABCMeta, abstractmethod
from app.models.dto.scrape_request import ScrapeRequestDTO

# Repository interface
class AuthServiceInterface(ABC):
    @abstractmethod
    def isAuth(self, token)->bool :
        pass