from app.strategy.retry_strategy import RetryStrategy
from app.utils.http_request_utils import make_http_request
from app import constants
import logging
import time

class SimpleRetryStrategy(RetryStrategy):
    def __init__(self):
        self.delay = constants.HTTP_REQUEST_RETRY_DELAY
        self.LOGGER = logging.getLogger(__name__)

    def make_request(self, method, url, **kwargs):        
        for cnt in range(2):
            try:
                resp = make_http_request(method, url)
                resp.raise_for_status()
                return resp
            except Exception as e:
                if(cnt == 1):
                    raise e;
                self.LOGGER.error("Unable to make scrape api call " + url + " Error " + str(e))
                self.LOGGER.info("Waiting for " + str(self.delay) + " sec for another retry")
                time.sleep(self.delay)
        