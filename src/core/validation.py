from datetime import timezone, timedelta
from fastapi import HTTPException
from sqlalchemy import func
from starlette import status
from datetime import datetime


def not_minus(val: int):
    if val <= 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Количество мест должно быть больше 0'
        )
    return val


def val_reservation(reservation_time: datetime, duration_minutes: int):
    now = datetime.now(tz=timezone.utc)
    end_time = reservation_time + timedelta(minutes=duration_minutes)
    if end_time > now:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Столик еще занят'
        )

