import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column (String(250), nullable= False)

class FavoriteCharacters (Base):
    __tablename__ = 'favoritecharacters'
    id = Column (Integer,primary_key=True)
    user_id = Column (Integer, ForeignKey('users.id'))
    character_id = Column(Integer, ForeignKey('characters.id'))

class FavoritePlanets (Base):
    __tablename__ = 'favoriteplanets'
    id = Column (Integer,primary_key=True)
    user_id = Column (Integer, ForeignKey('users.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))

class planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    planet_diameter = Column(String(250), nullable=False)
    planet_rotation_period = Column(String(250), nullable=False)
    planet_population = Column(Integer, nullable=False)
    planet_climate = Column(String(250), nullable=False)
    planet_terrain = Column(String(250), nullable=False)

class Characters (Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key = True)
    character_name = Column(String(250),nullable=False)
    character_gender = Column(String(250),nullable=False)
    character_skin_color = Column(String(250),nullable=False)
    character_birthdate = Column(String(250),nullable=False)
    character_eye_color = Column(String(250),nullable=False)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
