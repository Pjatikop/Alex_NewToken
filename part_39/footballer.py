from sqlalchemy import Column, Integer, String, ForeignKey
from part_39.database import Base

class Player(Base):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    surname = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    patronymic = Column(String(250), nullable=False)
    age = Column(Integer)
    team = Column(Integer, ForeignKey('teams.id'))

    def __init__(self, full_name, age, id_team):
        self.surname = full_name[0]
        self.name = full_name[1]
        self.patronymic = full_name[2]
        self.age = age
        self.team = id_team

    def __repr__(self):
        return f"Игрок (ФИО: {self.surname} {self.name} {self.patronymic}, возраст: {self.age}, " \
               f"ID команды: {self.team})"
