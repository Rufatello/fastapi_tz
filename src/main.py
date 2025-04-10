from fastapi import FastAPI
from src.routers.table import router as table_router
from src.routers.reservation import router as reservation_router
app = FastAPI()

app.include_router(table_router, prefix='/tables', tags=['tables'])
app.include_router(reservation_router, prefix='/reservations', tags=['reservations'])