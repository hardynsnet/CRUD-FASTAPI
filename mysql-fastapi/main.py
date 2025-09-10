import os 

from dotenv import load_dotenv

from fastapi import FastAPI, Depends, Query, HTTPException
from typing import Annotated
from sqlmodel import Field, Session, create_engine, select, SQLModel

load_dotenv()

# definir el modelo de sql y conexion
db_username = os.getenv('USER_DB')
db_password = os.getenv('PASSWORD_DB')
db_host = os.getenv('HOST_DB')
db_name = os.getenv('NAME_DB')

url_cn = f'mysql+pymysql://{db_username}:{db_password}@{db_host}:3306/{db_name}'
engine = create_engine(url_cn)

def create_db_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

session_dep = Annotated[Session, Depends(get_session)]

# Definiendo los modelos
class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)

class Hero(HeroBase, table=True):
    id: int = Field(default=None, primary_key=True)
    secret_name: str

class HeroPublic(HeroBase):
    id: int

class HeroCreate(HeroBase):
    secret_name: str

class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None

# API PATHS
app = FastAPI()

@app.get("/")
def bienvenidos():
    return {"mensaje":"Hola Mundo"}

@app.on_event('startup')
def on_startup():
    create_db_tables()

@app.post('/heroes/', response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: session_dep):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero

@app.get('/heroes/', response_model=list[HeroPublic])
def read_heroes(session: session_dep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100,):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes

@app.get('/heroes/{hero_id}', response_model=HeroPublic)
def read_hero(hero_id: int, session: session_dep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=400, detail='Hero not found')
    return hero

@app.patch('/heroes/{hero_id}', response_model=HeroPublic)
def update_hero(hero_id: int, hero: HeroUpdate, session: session_dep):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail='Hero not found')
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db

@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session: session_dep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail='Hero deleted or not found')
    session.delete(hero)
    session.commit()
    return {"ok": True}








