#!/usr/bin/python3
'''
Add new State object “Louisiana”
Usage : ./11-model_state_insert.py root root hbtn_0e_6_usa
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

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
