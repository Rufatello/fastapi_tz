from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.core.validation import not_minus
from src.models.restaurant import Table
from src.schemas.table import TableCreate, TableDelete


def list_table_rout(db: Session):
    return db.query(Table).all()


def create_table_rout(db: Session, user_data: TableCreate):
    val_seat = not_minus(user_data.seats)
    new_table = Table(
        name=user_data.name,
        seats=val_seat,
        location=user_data.location
    )
    db.add(new_table)
    db.commit()
    db.refresh(new_table)
    return new_table


def delete_table_rout(db: Session, user_data: TableDelete):
    table = db.query(Table).filter(Table.id == user_data.id).first()
    if not table:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Столик не найден'
        )
    db.delete(table)
    db.commit()
    return {"message": "Столик успешно удалён"}
