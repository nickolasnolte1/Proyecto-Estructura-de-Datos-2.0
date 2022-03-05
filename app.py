from flask import Flask, render_template, request, url_for, redirect
from flask.wrappers import Request
from functions import crear_usuario, printear_posts, users, agregar_intereses, i, printear_informacion, postsx, agregar_post

app = Flask(__name__)

@app.route('/' , methods = ["GET", "POST"])
def signup():
    username = request.args.get("username")
    email = request.args.get("email")
    password = request.args.get("password")
    confirm=request.args.get("confirm")
    if (username):
        if password==confirm:
            a, user_id=crear_usuario(username,i, email, password)
            return redirect(url_for('categories', user_id=user_id))
    return render_template('signup.html')

@app.route('/categories/<user_id>', methods = ["GET", "POST"])
def categories(user_id):
    if request.method == 'POST':
        interests=request.form.getlist('check')
        if (len(interests)>0):
            a, user_id=agregar_intereses(users, int(user_id), interests)
            return redirect(url_for('home', user_id=user_id))
    return render_template('categories.html')


@app.route('/homepage/<user_id>', methods = ["GET", "POST"])
def home(user_id):
    username, email, password, interests=printear_informacion(users,int(user_id))
    postinfo=printear_posts(postsx)
    if request.method == 'POST':
        post=request.form.get("post23")
        category=request.form.get('categories') 
        posts2=agregar_post(postsx,post, category)
        postinfo=printear_posts(posts2)
    return render_template('homepage.html', username=username, email=email, password=password, interests=interests, postinfo=postinfo)


if __name__ == "__main__":
    app.run(host="localhost", port = 8000, debug=True)
