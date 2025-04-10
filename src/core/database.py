from pydantic import BaseModel, PostgresDsn
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

from sqlalchemy.orm import sessionmaker

load_dotenv()
DB_USER = os.getenv("POSTGRES_USER")
DB_PASS = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = os.getenv("POSTGRES_PORT")


class DBConfig(BaseModel):
    host: str
    name: str
    password: str
    port: int
    user: str

    def dsn(self):
        return str(PostgresDsn.build(
            scheme='postgresql+psycopg2',
            host=self.host,
            username=self.user,
            port=self.port,
            path=self.name,
            password=self.password
        ))


class Settings(BaseModel):
    db: DBConfig


def get_settings():
    return Settings(
        db=DBConfig(
            host=DB_HOST,
            port=DB_PORT,
            password=DB_PASS,
            user=DB_USER,
            name=DB_NAME
        )
    )


settings = get_settings()

engine = create_engine(settings.db.dsn())
SessionLocale = sessionmaker(autoflush=False, bind=engine, autocommit=False)


def get_db():
    db = SessionLocale()
    try:
        yield db
    finally:
        db.close()
