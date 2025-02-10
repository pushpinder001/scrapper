from pydantic import BaseModel
from app.models.dto.scrape_request_metadata import ScrapeRequestMetaData

class ScrapeRequestDTO(BaseModel):
    target: str
    meta_data: ScrapeRequestMetaData
