import os
import sys
import datetime

from sqlalchemy import (
    Column, ForeignKey,
    Float, Integer, String, DateTime
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

 
Base = declarative_base()


class Server(Base):
    __tablename__ = "server"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    ip = Column(String(250), nullable=False)
    dt = DateTime(datetime.datetime.utcnow)


class Monitoring(Base):
    __tablename__ = "monitoring"
    id = Column(Integer, primary_key=True)
    ping = Column(Float, nullable=False)
    dt = DateTime(datetime.datetime.utcnow)
    server_id = Column(Integer, ForeignKey('server.id'))
    server = relationship(Server)

engine = create_engine('sqlite:///pymoni.db')
Base.metadata.create_all(engine)