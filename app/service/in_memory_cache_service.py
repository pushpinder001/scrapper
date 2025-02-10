from app.service.cache_service_interface import CacheServiceInterface
import json
import logging


class InMemoryCacheService(CacheServiceInterface):
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)
        self.data = {}

    def get(self, key) :
        return self.data.get(key)

    def put(self, key, value) :
        self.data[key] = value
