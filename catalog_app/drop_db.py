from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///car.db')

Base.metadata.reflect(engine)
Base.metadata.drop_all(engine)
