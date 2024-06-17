#!/usr/bin/python3
'''
List all State objects with corresponding City objects
Usage : ./101-relationship_states_cities_list.py root root hbtn_0e_101_usa
'''


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Instance = sessionmaker(bind=engine)
    session = Instance()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    session.close()
