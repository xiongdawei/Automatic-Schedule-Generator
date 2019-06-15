from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for, redirect,session, make_response, Response,config
from Function_A import function
import os
import hashlib

app = Flask(__name__)
# run the app connecting with the flask
app.config['SECRET_KET'] = os.urandom(24)
# Use the session of the broswer, configurate the secret key to a randomly generate 24 string

Base = declarative_base()
# declare a database
engine1 = create_engine('mysql+pymysql://root:@localhost:3306/classtime')
# connect the engine to the classtime database
DBSession = sessionmaker(bind = engine1)

engine2 = create_engine('mysql+pymysql://root:@localhost:3306/User_Data')
# connect the engine to the User_Data database
DBSession_A = sessionmaker(bind = engine2)

engine3 = create_engine('mysql+pymysql://root:@localhost:3306/basic')
DBSession_B = sessionmaker(bind = engine3)

class classslot(Base):
    __tablename__ = 'classslot'
    name = Column(String(200),primary_key=True,nullable= False, index = True)
    place = Column(Integer,primary_key=True,nullable= False, index = True)
    teacher = Column(String(200),primary_key=True,nullable = False, index = True)
    serial = Column(Integer,primary_key=True,nullable = False, index = True )
    week = Column(Integer,primary_key=True, nullable = False, index = True)

# Set up a class that is correspond to the database
# including the types of the database, the primary_key (for query), null, index


class user_data(Base):
    __tablename__ = 'user_data'
    Name = Column(String(50), primary_key=True, nullable=False, index=True)
    Email = Column(String(50), nullable=False, index=True)
    Password = Column(String(20), nullable=False, index=True)
    Group1 = Column(String(10), nullable=False, index=True)
    Group2 = Column(String(10), nullable=False, index=True)
    Group3 = Column(String(10), nullable=False, index=True)
    Group4 = Column(String(10), nullable=False, index=True)
    Group5 = Column(String(10), nullable=False, index=True)
    Group6 = Column(String(10), nullable=False, index=True)
    PE = Column(String(10), nullable=False, index=True)
    TOK = Column(String(10), nullable=False, index=True)
    Class = Column(Integer, nullable=False, index=True)

# Set up a class that is correspond to the database

class basic(Base):
    __tablename__ = 'basic'
    name = Column(String(20),primary_key=True,nullable=False, index=True)
    email = Column(String(20),nullable=False,index=True)
    password = Column(String(20),nullable=False,index=True)



class teacher():
    """
    This class is used to carry out operation for the teacher to retrieve and edit the dta
    """
    def __init(self):
        pass

    def retrieve(self,data):

