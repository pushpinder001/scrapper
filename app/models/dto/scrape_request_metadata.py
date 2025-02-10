from pydantic import BaseModel
from typing import Optional

class ScrapeRequestMetaData(BaseModel):
    num_pages: Optional[int] = 1
    field_name: Optional[list] = ['TITLE', 'PRICE', 'IMAGE_PATH']