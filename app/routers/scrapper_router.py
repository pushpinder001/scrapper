from fastapi import APIRouter, Depends, Header, HTTPException
from dependency_injector.wiring import inject, Provide
from typing import Optional
import logging
from app.containers.app_container import AppContainer
from app.controller.scrapper_controller import ScrapperController
from app.models.dto.scrape_request import ScrapeRequestDTO
from app.service.static_auth_service import StaticAuthService

"""
Endpoint to handle scraping requests.

Args:
    request_dto: Contains base URL and the number of pages to scrape.

Returns:
    Confirmation message with input details.
"""

class ScrapperRouter:
    def __init__(self):
        self.LOGGER = logging.getLogger(__name__)
        self.router = APIRouter()
        self.router.post("/scrape")(self.scrape_data)

    @inject
    def scrape_data(self, scrape_request: ScrapeRequestDTO, token: Optional[str] = Header(None),
            controller:ScrapperController = Depends(Provide[AppContainer.scrapper_controller]), 
            auth_service:StaticAuthService = Depends(Provide[AppContainer.auth_service])):
        self.LOGGER.info("Scrape Request: " + str(scrape_request))
        self.LOGGER.info("Token " + token)
        if(token is None or auth_service.isAuth(token) is False):
            self.LOGGER.error("Unauthorized token " + token)
            raise HTTPException(status_code=401, detail="UnAuthorized User")
        
        self.LOGGER.info("Calling handle_scraper_request")
        controller.handle_scraper_request(scrape_request)
        return {"message": "Scrapper successfully ran"}