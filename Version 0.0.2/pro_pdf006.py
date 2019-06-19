from flask import Flask, session, escape, request
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def set():
    session['username'] = 'liefyuan'
    return 'success'

@app.route('/get')
def get():
    return session.get('username')

@app.route('/delete/')
def delete():
    print(session.get('username'))
    session.pop('username')
    print(session.get('username'))
    return 'success'

@app.route('/delete')
def delete():


if __name__ == "__main__":
    app.run(debug=True)


