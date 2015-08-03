from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Make(Base):
    __tablename__ = 'make'

    id = Column(Integer, primary_key=True)
    company = Column(String(50), nullable=False)
    logo = Column(String, nullable=False)


class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    picture_url = Column(String)
    make_id = Column(Integer, ForeignKey('make.id'))
    make = relationship(Make)


class Specs(Base):
    __tablename__ = 'specs'

    id = Column(Integer, primary_key=True)
    price = Column(String)
    hp = Column(String)
    mpg = Column(String)
    car_id = Column(Integer, ForeignKey('model.id'))
    car = relationship(Model)
    make_id = Column(Integer, ForeignKey('make.id'))
    make = relationship(Make)

engine = create_engine('sqlite:///car.db')

Base.metadata.create_all(engine)
