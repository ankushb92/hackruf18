from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///a.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    loginName = Column(String)
    roleType = Column(String)
    session = Column(Text)
    age = Column(Integer)
    

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
