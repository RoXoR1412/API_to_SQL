from typing import Optional
from sqlmodel import SQLModel, Field, create_engine, Session, select

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
hero_3= Hero(name="Tarantula", secret_name="Natalia Roman-on", age=32)
hero_4 = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)

engine=create_engine("sqlite:///database.db")
SQLModel.metadata.create_all(engine)

with Session(engine) as session:
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    session.add(hero_4)
    session.commit()

with Session(engine) as session:
    statement = select(Hero)
    heroes = session.exec(statement)
    for hero in heroes:
        print(hero)