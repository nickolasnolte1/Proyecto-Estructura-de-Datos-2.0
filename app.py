from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import psycopg2


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('signup.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['username']
    processed_text = text.upper()
    return processed_text



if __name__ == "__main__":
    app.run(host="localhost", port = 8000, debug=True)