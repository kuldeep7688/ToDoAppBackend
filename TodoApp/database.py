from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # we will only allow one thread to communicate with SQL
    # assuming that each thread handles an independent request
    # to prevent any type of accidental sharing of the same connection between different request
    # since there could be multiple threads happening towards the same database
    # so sqllite should check multiple threads
    connect_args={"check_same_thread": False}

)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False,
    bind=engine
)

Base = declarative_base()
