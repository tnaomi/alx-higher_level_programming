#!/usr/bin/python3
'''
State name passed as arg, Returns ID or error
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

    state = session.query(State).filter(State.name == argv[4]).first()
    print('Not found' if not state else state.id)
    session.close()
