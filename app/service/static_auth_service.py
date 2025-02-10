from app.service.auth_service_interface import AuthServiceInterface
import json
import logging
from app import constants


class StaticAuthService(AuthServiceInterface):
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)
        self.token = constants.TOKEN

    def isAuth(self, token)->bool :
        return self.token == token
