from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for, redirect,session, make_response, Response,config
from Function_A import Function_A
import os
import hashlib

app = Flask(__name__)
# run the app connecting with the flask
app.config['SECRET_KET'] = os.urandom(24)
# Use the session of the broswer, configurate the secret key to a randomly generate 24 string

Base = declarative_base()
# declare a database
engine1 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/classtime')
# connect the engine to the classtime database
DBSession = sessionmaker(bind = engine1)

engine2 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/User_Data')
# connect the engine to the User_Data database
DBSession_A = sessionmaker(bind = engine2)

engine3 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/basic')
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

# This is the database for users to sign up

# This a class that aim for the operation related with users' log in
# Including the registration date
# This class includes a wide range of functions including data fetch and user verification

class Function_B():
    def __init(self):
        pass


    def encrypt(self,password):
        """
        :param password: This is the password input
        :return: An encrypted password that will be permenantly stored in the database
        """
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        return hl.hexdigest()

    def check_password(self,password):
        """
        :param password: This is the password that the user input
        :return: Boolean expression, whether the users' input is right or not
        """
        hll = hashlib.md5()
        hll.update(password.encode(encoding='utf-8'))

    def check_psd(self,name,password):
        b = Function_B()
        session = DBSession_B()
        password = b.encrypt(password)
        try:
            encrypted_password = session.query(basic).filter(basic.name == name).first()
        except:
            return False
        if password == encrypted_password.password:
            return True
        else:
            return False

    def add_user_data(self,data):
        session = DBSession_B()
        session.add(data)
        session.commit()
        session.close()

    def fetch_user_data(self,data):
        session = DBSession_B()
        results = session.query(basic).filter(basic.name == data).one()
        return results.password


    def find_user_psw(self,name):
        session = DBSession_B()
        results = session.query(basic).filter(basic.name == name).one()
        return results.password

    def check_email_repeatition(self,name,email):
        session = DBSession_B()
        results = session.query(basic).filter(basic.name == name).all()
        listt = []
        for i in results:
            listt.append(i.email)
        if email in listt:
            return False
        else:
            return True

    def check_username_repeatition(self,name):
        session = DBSession_B()
        results = session.query(basic).filter(basic.name == name).all()
        listt = []
        for i in results:
            listt.append(i.name)
        if name in listt:
            return False
        else:
            return True

"""
a = Function_B()
psw = 'abcd'
psw = a.encrypt(psw)
data = basic(name='Daaavid',email = 'davidxiong@sina.cn',password =psw)
a.add_user_data(data)
"""
