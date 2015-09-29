from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///car.db')

# Drops database when executed from command line
Base.metadata.reflect(engine)
Base.metadata.drop_all(engine)
