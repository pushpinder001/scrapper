from abc import ABC, ABCMeta, abstractmethod

# Repository interface
class ProductHtmlTagParserStrategy(ABC):
    @abstractmethod
    def parse(metaData):
        pass