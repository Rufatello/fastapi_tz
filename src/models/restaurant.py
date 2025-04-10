from datetime import timezone
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime, func
from enum import Enum as PyEnum

from sqlalchemy.orm import relationship

from src.models.base import Base


class Location(str, PyEnum):
    THE_WINDOW = 'the_window'
    THE_HALL = 'the_hall'
    TERRACE = 'terrace'


class Table(Base):
    __tablename__ = 'table'
    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(50))
    seats = Column(Integer)
    location = Column(Enum(Location), default=Location.THE_HALL)
    reservations = relationship("Reservation", back_populates="table")


class Reservation(Base):
    __tablename__ = 'reservation'
    id = Column(Integer, index=True, primary_key=True)
    customer_name = Column(String(50))
    table_id = Column(ForeignKey(Table.id), nullable=False)
    reservation_time = Column(DateTime(timezone=True), server_default=func.now(tz=timezone.utc))
    duration_minutes = Column(Integer)
    table = relationship("Table", back_populates="reservations")
