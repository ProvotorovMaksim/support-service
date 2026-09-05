from pydantic import BaseModel
from datetime import datetime
from models import TicketStatus

class TicketCreate(BaseModel):
    subject: str
    message: str

class TicketResponse(BaseModel):
    id: int
    subject: str
    message: str
    status: TicketStatus
    created_at: datetime

    class Config:
        from_attributes = True
