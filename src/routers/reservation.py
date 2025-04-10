from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controllers.reservation import list_reservation_rout, create_reservation_rout, delete_reservation_rout
from src.core.database import get_db
from src.schemas.reservation import ReservationResponse, ReservationCreate, ReservationDelete

router = APIRouter()


@router.get('/', response_model=List[ReservationResponse], status_code=200)
def list_tables(db: Session = Depends(get_db)):
    return list_reservation_rout(db=db)


@router.post('', response_model=ReservationResponse, status_code=201)
def create_reservation(user_data: ReservationCreate, db: Session = Depends(get_db)):
    return create_reservation_rout(db=db, user_data=user_data)


@router.delete('', status_code=200)
def delete_reservation(user_data: ReservationDelete, db: Session = Depends(get_db)):
    return delete_reservation_rout(user_data=user_data, db=db)
