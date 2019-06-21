from flask import Flask, session, app, render_template, redirect
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)
