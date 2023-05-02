from part_39.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    team_name = Column(String(250), nullable=False)
    player = relationship('Player')

    def __repr__(self):
        return f"Команда (ID: {self.id}, название: {self.team_name})"
