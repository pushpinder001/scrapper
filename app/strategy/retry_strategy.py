from abc import ABC, ABCMeta, abstractmethod

# Repository interface
class RetryStrategy(ABC):
    @abstractmethod
    def make_request(method, url, **kwargs):
        pass
