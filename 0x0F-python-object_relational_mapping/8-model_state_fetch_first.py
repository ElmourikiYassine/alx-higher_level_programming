#!/usr/bin/python3
"""
 prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    state = session.query(State).first()

    if state:
        print('{}: {}'.format(state.id, state.name))
    else:
        print("Nothing")

    session.close()
