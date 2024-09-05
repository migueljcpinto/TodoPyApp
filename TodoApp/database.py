from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# This URL is going to be used to be able to create a location of this database on our fastAPI application.
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:7895123@localhost/TodoApplicationDatabase'
SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:7895123@127.0.0.1:3306/TodoApplicationDatabase'

# Creating an engine for the application
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base which is an object of the database which is going to be able to then control our database.
Base = declarative_base()
