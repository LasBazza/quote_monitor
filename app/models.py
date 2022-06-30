from sqlalchemy import Column, String, Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.core.db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    created = Column(DateTime)
    is_active = Column(Boolean, default=False)

    favorite_list = relationship('FavoriteList', back_populates='user')


class FavoriteList(Base):
    __tablename__ = 'favorite_list'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    user = relationship('User', back_populates='favorite_list')
