import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine


Base = declarative_base()



class Titles(Base):
    __tablename__ = 'Titles'
    id = Column(Integer, primary_key=True)
    titles = Column(String, nullable=False)
 
class Prices(Base):
    __tablename__ = 'Prices'
    id = Column(Integer, primary_key=True)
    prices = Column(String, nullable=False)

class AddDate(Base):
    __tablename__ = 'AddDate'
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
 



# Create an engine that stores data in the local directory's
engine = create_engine('sqlite:///CenyKsiazek.db')

# Create all tables in the engine. This is equivalent to "Create Table"
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker


Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()
