from abc import ABC, ABCMeta, abstractmethod

# Repository interface
class ProductRepositoryInterface(ABC):
    @abstractmethod
    def save_product(self, product: map) -> None:
        pass

    @abstractmethod
    def get_product_by_name(self, product_name):
        pass