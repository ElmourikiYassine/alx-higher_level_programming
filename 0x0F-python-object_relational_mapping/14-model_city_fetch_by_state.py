#!/usr/bin/python3
"""
change the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()

    city = session.query(State, City).join(City).order_by(City.id)

    for state, city in city:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
