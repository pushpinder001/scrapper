from pydantic import BaseModel
from typing import Optional

class ScrapeRequestDTO(BaseModel):
    num_pages: Optional[int] = 1
    proxy_string: str = None
