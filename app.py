from distutils.log import debug
from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from jinja2 import Template, FileSystemLoader, Environment
from sympy import true
from functions import agregar_intereses, crear_usuario

app = Flask(__name__)

@app.route('/' , methods = ["GET", "POST"])
def signup():
    username = request.args.get("username")
    email = request.args.get("email")
    password = request.args.get("password")
    confirm=request.args.get("confirm")
    if (username):
        if password==confirm:
            user=crear_usuario(username,email,password)
            return redirect(url_for('categories', user=user))
    return render_template('signup.html')

@app.route('/categories/<user>', methods = ["GET", "POST"])
def categories(user):
    if request.method == 'POST':
        interests=request.form.getlist('check')
        if (len(interests)>0):
            user=agregar_intereses(user,interests)
            return redirect(url_for('home', user=user))
    return render_template('categories.html')

@app.route('/homepage/<user>')
def home(user):
    return render_template('homepage.html')

if __name__ == "__main__":
    app.run(host="localhost", port = 8000, debug=True)
