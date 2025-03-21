from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from ..models.chat import Base
from ..config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def init_db():
    """Initialize the database"""
    Base.metadata.create_all(engine)

def get_db_session():
    """Get a scoped database session"""
    return Session()

def close_db_session():
    """Close the current database session"""
    Session.remove()
