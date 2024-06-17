#!/usr/bin/python3
'''
Update a State object
Usage : ./12-model_state_update_id_2.py root root hbtn_0e_6_usa
        ./7-model_state_fetch_all.py root root hbtn_0e_6_usa
'''


from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Instance = sessionmaker(bind=engine)
    session = Instance()

    states = session.query(State).filter(State.id == 2)

    for el in states:
        el.name = 'New Mexico'

    session.commit()
    session.close()
