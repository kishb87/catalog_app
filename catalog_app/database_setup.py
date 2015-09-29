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

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
        }


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

    @property
    def serialize(self):
        return {
            'id': self.id,
            'price': self.price,
            'hp': self.hp,
            'mpg': self.mpg,
            'car_id': self.car_id,
            'make_id': self.make_id,
        }

engine = create_engine('sqlite:///car.db')

# Creates database when executed from command line
Base.metadata.create_all(engine)
