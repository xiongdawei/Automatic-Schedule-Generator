from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for, redirect
from flask_script import Manager
from Function_A import Function_A
import hashlib

app = Flask(__name__)
Base = declarative_base()
engine1 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/classtime')
DBSession = sessionmaker(bind = engine1)

engine2 = create_engine('mysql+pymysql://root:cykablyat@localhost:3306/User_Data')
DBSession_A = sessionmaker(bind = engine2)

engine3 = create_engine('mysql+pymysql://root;cykablyat@localhost:3306/teacher')
DBSession_C = sessionmaker(bind=engine3)

class classslot(Base):
    __tablename__ = 'classslot'
    name = Column(String(200),primary_key=True,nullable= False, index = True)
    place = Column(Integer,primary_key=True,nullable= False, index = True)
    teacher = Column(String(200),primary_key=True,nullable = False, index = True)
    serial = Column(Integer,primary_key=True,nullable = False, index = True )
    week = Column(Integer,primary_key=True, nullable = False, index = True)

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

class teacher(Base):
    __tablename__ = 'teacher'
    name = Column(String(30),primary_key=True, nullable=False,index=True)
    email = Column(String(30),nullable=False,index=True)
    password = Column(String(30),nullable=False,index=True)


class Function_E():
    def __init__(self):
        pass

    def add_user_date(self,data):
        session = DBSession_C()
        session.add(data)
        session.commit()
        session.close()


a = Function_E()
b = Function_A()

#results = b.get_user_datacurrent('cynthia')
#print(results)
#result = b.serach_byname('English SL')
#print(result)





