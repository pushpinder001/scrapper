from fastapi import HTTPException, Depends
from typing import List
import logging
from app.models.dto.scrape_request import ScrapeRequestDTO
from app.models.scrapper_target import ScrapperTarget

class ScrapperController:
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
        self.LOGGER = logging.getLogger(__name__)

    def handle_scraper_request(self, scrape_request: ScrapeRequestDTO) -> dict:
        self.LOGGER.info("Entered handle_scraper_request")
        self.LOGGER.info("Scrape Request " + str(scrape_request))

        if scrape_request.proxy_string is None :
            raise HTTPException(status_code=400, detail="proxy_string field not found in input")

        scrapping_meta_data = {}

        scrapper_meta_data_entries = scrape_request.proxy_string.split(' ')
        for scrapper_meta_data_entry in scrapper_meta_data_entries :
            key_val = scrapper_meta_data_entry.split(':')
            scrapping_meta_data[key_val[0]] = key_val[1]

        if("TARGET" not in scrapping_meta_data):
            raise HTTPException(status_code=400, detail="Target not found in proxy_string")
        print(scrapping_meta_data)

        target = scrapping_meta_data["TARGET"]

        if(target in self.dispatcher["modules"]) :
            service = self.dispatcher["modules"][target]
            self.LOGGER.info("Running scrapper")
            service.run(scrape_request, ScrapperTarget[target])
        else:
            raise HTTPException(status_code=404, detail="Target not found")