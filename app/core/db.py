from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

SQLALCHEMY_DATABASE_URL = ('postgresql://' + settings.DB_USER + ':' + settings.DB_PASSWORD + '@localhost:' +
                           str(settings.DB_PORT) + '/' + settings.DB_NAME)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
