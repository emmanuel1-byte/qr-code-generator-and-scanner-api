from pydantic import BaseModel
from typing import Optional

class QrCode(BaseModel):
    content: str
    background_color: Optional[str] = "white"