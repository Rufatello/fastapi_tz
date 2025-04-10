from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.controllers.table import list_table_rout, create_table_rout, delete_table_rout
from src.core.database import get_db
from src.schemas.table import TableResponse, TableCreate, TableDelete

router = APIRouter()


@router.get('/', response_model=List[TableResponse], status_code=200)
def list_tables(db: Session = Depends(get_db)):
    return list_table_rout(db=db)


@router.post('', response_model=TableResponse, status_code=201)
def create_table(user_data: TableCreate, db: Session = Depends(get_db)):
    return create_table_rout(db=db, user_data=user_data)


@router.delete('', status_code=200)
def delete_table(user_data: TableDelete, db: Session = Depends(get_db)):
    return delete_table_rout(db=db, user_data=user_data)
