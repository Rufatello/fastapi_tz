from datetime import datetime
from pydantic import BaseModel


class ReservationCreate(BaseModel):
    customer_name: str
    table_id: int
    duration_minutes: int


class ReservationDelete(BaseModel):
    id: int


class ReservationResponse(BaseModel):
    id: int
    customer_name: str
    table_id: int
    duration_minutes: int
    reservation_time: datetime
