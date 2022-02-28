from distutils.log import debug
from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from sympy import true
from functions import crear_usuario

app = Flask(__name__)

@app.route('/' , methods = ["GET", "POST"])
def signup():
    if request.method=="POST":
        users=[]
        username = request.args.get("username")
        email = request.args.get("email")
        password = request.args.get("password")
        confirm=request.args.get("confirm")
        if password==confirm:
            #users=crear_usuario(users,username,email,password)
            return redirect ("localhost:8000/categories")
    return render_template('signup.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')


if __name__ == "__main__":
    app.run(host="localhost", port = 8000, debug=True)