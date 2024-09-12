from pydantic import BaseModel
from typing import Optional

class QrCode(BaseModel):
    content: str
    fill_color: Optional[str] = "black"
    background_color: Optional[str] = "white"