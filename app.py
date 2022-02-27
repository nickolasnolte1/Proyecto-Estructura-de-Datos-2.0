from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from typing import Dict, Text
import psycopg2


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('Homepage.html')

if __name__ == "__main__":
    app.run(host="localhost", port = 8000, debug=True)