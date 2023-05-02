from faker import Faker
from part_39.database import create_db, Session
from part_39.footballer import Player
from part_39.team import Team

def create_database(load_fake_data=True):
    create_db()
    if load_fake_data:
        _load_fake_data(Session())

def _load_fake_data(session):
    team1 = Team(team_name='ЦСК')
    team2 = Team(team_name='Зенит')
    session.add(team1)
    session.add(team2)

    faker = Faker('ru_RU')

    team_list = [team1, team2]

    session.commit()

    for _ in range(22):
        full_name = faker.name().split()
        age = faker.random.randint(18, 28)
        team = faker.random.choice(team_list)

        player = Player(full_name, age, team.id)
        session.add(player)

    session.commit()
    session.close()
