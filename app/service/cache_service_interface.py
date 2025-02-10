from abc import ABC, ABCMeta, abstractmethod

# Repository interface
class CacheServiceInterface(ABC):
    @abstractmethod
    def get(self, key) :
        pass

    @abstractmethod
    def put(self, key, value) :
        pass
