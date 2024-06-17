#!/usr/bin/python3
'''
Delete all State objects with name containing 'a'
Usage : ./13-model_state_delete_a.py root root hbtn_0e_6_usa
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

    states = session.query(State).filter(State.name.contains('a')).all()

    for state in states:
        session.delete(state)

    session.commit()
    session.close()
