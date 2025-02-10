import requests
import logging

LOGGER = logging.getLogger(__name__)

def make_http_request(method, url, **kwargs):
    """
    Makes an HTTP request with the specified method, URL, and optional parameters.

    Args:
        method (str): The HTTP method (e.g., "GET", "POST", "PUT", "DELETE").
        url (str): The URL to send the request to.
        **kwargs: Additional keyword arguments to pass to the requests.request() method.
                 This can include parameters like headers, data, json, etc.

    Returns:
        requests.Response: The response object.
    """
    LOGGER.info("method " + str(method) + " url " + str(url) + " K " + str(kwargs))
    response = requests.request(method, url, **kwargs)
    return response