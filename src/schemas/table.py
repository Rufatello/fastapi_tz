from enum import Enum

from pydantic import BaseModel


class Location(str, Enum):
    THE_WINDOW = 'the_window'
    THE_HALL = 'the_hall'
    TERRACE = 'terrace'


class TableCreate(BaseModel):
    name: str
    seats: int
    location: Location


class TableDelete(BaseModel):
    id: int


class TableResponse(BaseModel):
    id: int
    name: str
    seats: int
    location: Location
