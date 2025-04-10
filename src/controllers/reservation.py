import random
from datetime import timezone, datetime

from fastapi import HTTPException
from sqlalchemy import func
from sqlalchemy.orm import Session
from starlette import status
from src.core.validation import not_minus, val_reservation
from src.models.restaurant import Table, Reservation
from src.schemas.reservation import ReservationCreate, ReservationDelete


def list_reservation_rout(db: Session):
    return db.query(Reservation).all()


def create_reservation_rout(db: Session, user_data: ReservationCreate):
    table = db.query(Table).filter(Table.id == user_data.table_id).first()
    if not table:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Столик не найден'
        )
    active_reservation = db.query(Reservation).filter(Reservation.table_id == user_data.table_id).first()
    if active_reservation:
        val_reservation(active_reservation.reservation_time, active_reservation.duration_minutes)
    new_reservation = Reservation(
        table_id=user_data.table_id,
        customer_name=user_data.customer_name,
        duration_minutes=random.randint(10, 100),
        reservation_time=datetime.now(tz=timezone.utc)
    )
    db.add(new_reservation)
    db.commit()
    db.refresh(new_reservation)
    return new_reservation


def delete_reservation_rout(db: Session, user_data: ReservationDelete):
    reservation = db.query(Reservation).filter(Reservation.id == user_data.id).first()
    if not reservation:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Нет такой резервации'
        )
    db.delete(reservation)
    db.commit()
    return {"message": "Резервация удалена"}
