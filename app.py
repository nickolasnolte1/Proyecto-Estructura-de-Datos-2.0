from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import psycopg2
from functions import crear_usuario

users=[]
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('signup.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/', methods=['POST'])
def my_form_post():
    username = request.form['username']
    email=request.form['email']
    password=request.form['password']
    confirm=request.form['confirm']
    if password==confirm:
        users=crear_usuario(users, username, email, password)
        return users
    else:
        return "error"



if __name__ == "__main__":
    app.run(host="localhost", port = 8000, debug=True)