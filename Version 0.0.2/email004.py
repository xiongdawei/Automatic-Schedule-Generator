from flask import Flask, session, config
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def set():
    session['username'] = 'username'
    return 'success'

@app.route('/get')
def get():
    session['username']
    session.get('username')
    return session.get('username')

@app.route('/delete')
def delete():
    session.pop('username')
    session.clear()
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
