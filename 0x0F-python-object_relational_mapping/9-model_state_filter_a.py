#!/usr/bin/python3
'''
list all State objects that containing 'a'
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

    states = session.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
    session.close()


# ./9-model_state_filter_a.py root root hbtn_0e_6_usa
# You must import State and Base from model_state -
# ...from model_state import Base, State
# Results must be sorted in ascending order by states.id
