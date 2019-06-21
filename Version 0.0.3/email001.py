from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/register',methods=['POST'])
def register():
    print(request.headers)
    print(request.stream.read())
    return 'welcome'

if __name__ == '__main__':
    app.run(debug=True)
