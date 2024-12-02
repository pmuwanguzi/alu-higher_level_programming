#!/usr/bin/python3
"""List all states"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create the engine and bind it to the session
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Iterate over the query results directly without fetching all at once
    query = session.query(State).order_by(State.id)
    for state in query:  # Fetch results lazily
        print("{}: {}".format(state.id, state.name))

    session.close()
