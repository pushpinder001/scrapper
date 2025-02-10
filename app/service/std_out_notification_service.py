from app.service.notification_service_interface import NotificationServiceInterface
import json
import logging

class StdOutNotificationService(NotificationServiceInterface):
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)

    def notify(self, notificationMetaData) -> None :
        self.LOGGER.info("Sending notification " + notificationMetaData);