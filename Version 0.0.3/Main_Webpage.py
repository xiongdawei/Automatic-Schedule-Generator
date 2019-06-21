from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, render_template, request, url_for,redirect,session, make_response, Response,config
from Function_A import Function_A
from Function_B import Function_B
from datetime import timedelta
import os
import execjs
import pyexec

app = Flask(__name__)
# run the app connecting with the flask
app.config['SECRET_KEY'] = os.urandom(24)

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

@app.route('/',methods=['POST','GET'])
def log_in():
    if request.method == 'POST':
        b = Function_B()
        name = request.form.get('username')
        password = request.form.get('psw')
        if b.check_psd(name,password) == True:
#            session['username'] = name
#            session['password'] = password
            if b.check_property(name) == 'student':
                session['username'] = name
                return redirect('/preference')
            else:
                session['username'] = name
                return redirect('/teacher')
        else:
            return 'The password is not correct'
    else:
        return render_template('log_in001.html')

@app.route('/teacher',methods=['POST','GET'])
def teacher():
    a = Function_A()
    name = session.get('username')
    listt = a.search_all()
    return render_template('teacher.html', Doc001 = name, data = listt)



@app.route('/sign_up',methods=['POST','GET'])
def sign_up():
    if request.method == 'POST':
        b = Function_B()
        name = request.form.get('username')
        email = request.form.get('email')
        psw = request.form.get('psw')
        psw_rec = request.form.get('psw_reconfirm')
        if psw_rec == psw:
            if b.check_email_repeatition(name,email) == True:
                if b.check_username_repeatition(name) == True:
                    psw = b.encrypt(psw)
                    data = basic(name=name,email=email,password= psw)
                    b.add_user_data(data)
                else:
                    return 'This username has already been used'
            else:
                return 'This email has already been registered'
            b.add_user_data(data)
            session['username'] = name
            return  redirect('/result')
        else:
            return "The passwords are not consistent"


    else:
        return render_template('sign_up001.html')


@app.route('/preference', methods=["POST","GET"])
def choose():
    NAMME = session.get('username')
    session['uesr'] = NAMME
    if request.method == 'POST':
        # Use the class: Function_A and Function_B
        a = Function_A()
        b = Function_B()
        namee = NAMME
        email = b.fetch_user_email(NAMME)
        password = session.get('password')
        group1 = request.form.get('group1')
        group2 = request.form.get('group2')
        group3 = request.form.get('group3')
        group4 = request.form.get('group4')
        group5 = request.form.get('group5')
        group6 = request.form.get('group6')
        pe = request.form.get('pe')
        tok = request.form.get('TOK')
        classs = request.form.get('class')
        data = user_data(Name=namee,Email=email,Password=password,Group1=group1,Group2=group2,
                         Group3=group3,Group4=group4,Group5=group5,Group6=group6,PE=pe,TOK=tok,Class=classs)
        a.add_user_data(data)
        session['username'] = NAMME

        return redirect('/result')
    else:
        return render_template('Test002.html',Doc001=NAMME)


@app.route('/result')
def index():
    NAME = session.get('username')
    a = Function_A()
    lalala = a.select_choice_new(NAME)
    result10 = a.specify(lalala,1,1)
    result11 = a.specify(lalala,2,1)
    result12 = a.specify(lalala,3,1)
    result13 = a.specify(lalala,4,1)
    result15 = a.specify(lalala,6,1)
    result16 = a.specify(lalala,7,1)
    result17 = a.specify(lalala,8,1)
    result18 = a.specify(lalala,9,1)
    result20 = a.specify(lalala,1,2)
    result21 = a.specify(lalala,2,2)
    result22 = a.specify(lalala,3,2)
    result23 = a.specify(lalala,4,2)
    result25 = a.specify(lalala,6,2)
    result26 = a.specify(lalala,7,2)
    result27 = a.specify(lalala,8,2)
    result28 = a.specify(lalala,9,2)
    result30 = a.specify(lalala,1,3)
    result31 = a.specify(lalala,2,3)
    result32 = a.specify(lalala,3,3)
    result33 = a.specify(lalala,4,3)
    result35 = a.specify(lalala,6,3)
    result36 = a.specify(lalala,7,3)
    result37 = a.specify(lalala,8,3)
    result38 = a.specify(lalala,9,3)
    result40 = a.specify(lalala,1,4)
    result41 = a.specify(lalala,2,4)
    result42 = a.specify(lalala,4,4)
    result43 = a.specify(lalala,5,4)
    result45 = a.specify(lalala,6,4)
    result46 = a.specify(lalala,7,4)
    result47 = a.specify(lalala,8,4)
    result50 = a.specify(lalala,1,5)
    result51 = a.specify(lalala,2,5)
    result52 = a.specify(lalala,4,5)
    result53 = a.specify(lalala,5,5)
    result55 = a.specify(lalala,6,5)
    result56 = a.specify(lalala,7,5)
    result57 = a.specify(lalala,8,5)
    result58 = a.specify(lalala,9,5)

    return render_template('timetable.html',mon10 = result10, mon11 = result11,mon12=result12,mon13=result13,
                           mon15=result15,mon16=result16,mon17=result17,mon18=result18,mon20=result20,
                           mon21=result21,mon22=result22,mon23=result23,mon25=result25,mon26=result26,mon27=result27,mon28=result28,
                           mon30=result30,mon31=result31,mon32=result32,mon33=result33,mon35=result35,mon36=result36,mon37=result37,mon38=result38,
                           mon40=result40,mon41=result41,mon43=result42,mon44=result43,mon45=result45,mon46=result46,mon47=result47,
                           mon50=result50,mon51=result51,mon53=result52,mon54=result53,mon55=result55,mon56=result56,mon57=result57,mon58=result58, Doc001=NAME)

if __name__=='__main__':
    app.run(debug=True)

