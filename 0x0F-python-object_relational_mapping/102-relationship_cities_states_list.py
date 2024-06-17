#!/usr/bin/python3
"""
List all City objects from the database hbtn_0e_101_usa
Format : <city id>: <city name> -> <state name>
Usage : ./102-relationship_cities_states_list.py root root hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Instance = sessionmaker(bind=engine)
    Session = Instance()

    state_query = Session.query(State).join(City).order_by(City.id).all()

    for state in state_query:
        for city in state.cities:
            print("{}: {} -> {}".format(city.id, city.name, state.name))
