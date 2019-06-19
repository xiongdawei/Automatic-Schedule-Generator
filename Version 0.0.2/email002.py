from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for, redirect,session, make_response, Response,config
from Function_A import Function_A
from Function_B import Function_B
import os
import execjs
import pyexec

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

class basic(Base):
    __tablename__ = 'basic'
    name = Column(String(20),primary_key=True,nullable=False, index=True)
    email = Column(String(20),nullable=False,index=True)
    password = Column(String(20),nullable=False,index=True)

# This is the database for users to sign up

name = "davidxiong"

@app.route('/',methods=['POST','GET'])
def log_in():
    if request.method == 'POST':
        return render_template('log_in001.html')
    else:
        username = request.form.get('username')
        password = request.form.get('psw')

if __name__=='__main__':
    app.run(debug=True)

