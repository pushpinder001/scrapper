from fastapi import HTTPException, Depends
from typing import List
import logging
from app.models.dto.scrape_request import ScrapeRequestDTO
from app.models.scrapper_target import ScrapperTarget
from app.service.scrapper_service import ScrapperService

class ScrapperController:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.LOGGER = logging.getLogger(__name__)

    def handle_scraper_request(self, scrape_request: ScrapeRequestDTO) -> dict:
        self.LOGGER.info("Entered handle_scraper_request")
        self.LOGGER.info("Scrape Request " + str(scrape_request))

        if(scrape_request.target in self.dispatcher["modules"]) :
            service = self.dispatcher["modules"][scrape_request.target]
            self.LOGGER.info("Running scrapper")
            service.run(scrape_request, ScrapperTarget[scrape_request.target])
        else:
            raise HTTPException(status_code=404, detail="Target not found")