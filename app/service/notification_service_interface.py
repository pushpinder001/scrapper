from abc import ABC, ABCMeta, abstractmethod

# Repository interface
class NotificationServiceInterface(ABC):
    @abstractmethod
    def notify(self, notificationMetaData):
        pass