from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
DB_URL = "postgresql+psycopg://sd4:sd4@localhost:5432/board"
engine = create_engine(DB_URL)
# engine = create_engine(DB_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
def home():
    return {'hello': 'hi'}