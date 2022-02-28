from distutils.log import debug
from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from sympy import true
from functions import crear_usuario

app = Flask(__name__)
users=[]

@app.route('/' , methods = ["GET", "POST"])
def homepage():
    if (request.method=="POST"):
        username = request.form['username']
        email=request.form['email']
        password=request.form['password']
        confirm=request.form['confirm']
        if password==confirm:
            users=crear_usuario(users, username, email, password)
            return redirect('http://localhost:8000/categories', code=302)
    return render_template('signup.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')


if __name__ == "__main__":
    app.run(host="localhost", port = 8000, debug=True)