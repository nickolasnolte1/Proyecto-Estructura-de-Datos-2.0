from flask import Flask, render_template, request, url_for, redirect, flash, Response
from flask.wrappers import Request
from functions import crear_usuario, printear_notifications, printear_posts, users, agregar_intereses, postsx, check, notifications, updatear_posts, info_username, BinarySearch
import re
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO

matplotlib.use('Agg')

#para verificar el formato del email. 
regex = r'\b[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

app = Flask(__name__)
app.config['DEBUG'] = True




def check(email):
	if(re.fullmatch(regex, email)):
		return "Valid Email"
	else:
		return "Invalid Email"



@app.route('/profile/<userexists>')
def profile (userexists):
    username, email, interests=info_username(users,userexists)
    return render_template('profile.html', username=username, email=email, interests=interests)

@app.route('/' , methods = ["GET", "POST"])
def signup():
    username = request.args.get("username")
    email = request.args.get("email")
    password = request.args.get("password")
    confirm=request.args.get("confirm")
    if (username):
        if check(email)=="Valid Email":
            if password==confirm:
                a, user_id=crear_usuario(username, email, password)
                return redirect(url_for('categories', user_id=user_id))
            else:
                flash("Passwords don't match", "warning")
        else:
            flash("Invalid email address", "warning")
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
    username, email, password, interests=BinarySearch(users,int(user_id))
    postinfo=printear_posts(postsx)
    notifs=printear_notifications(notifications)
    if request.method == 'POST':
        if request.form['btn']=='Accept':
            friend="danielbehar"
            users.graph_edge(username, friend)
            users.graph_edge(friend, username)
            users.disp_graph()
            users.generate_edges()
        if request.form['btn']=='post':
            post=request.form.get("post23")
            category=request.form.get('categories')
            minutes=request.form.get('datetopost')
            postsx.insert(post,category, minutes)
            if int(minutes)>0:
                notifications.push(f"Post will be published in {minutes} minutes.")
            else:
                notifications.push("Post was published Successfully!")
            postinfo=updatear_posts(postsx)
            notifs=printear_notifications(notifications)
        if request.form['btn']=='findfriend':
            friend=request.form.get('friendtofind')
            userexists=users.search_user(username,friend)
            if userexists:
                return redirect(url_for('profile', userexists=userexists))
    return render_template('homepage.html', username=username, email=email, password=password, interests=interests, postinfo=postinfo, notifs=notifs)


plt.rcParams["figure.figsize"] = [20, 12]
plt.rcParams["figure.autolayout"] = True
@app.route('/print-plot')
def plot_png():
    G = nx.DiGraph()  
    G.add_edges_from(users.edges) 
    vals=[]
    val_map={}
    x=10.0
    for name in users.edges:
        vals+=name[0]
    values = [val_map.get(node, 0.80) for node in G.nodes()]
    black_edges = [edge for edge in G.edges()]
    cmap = matplotlib.colors.ListedColormap(['C0', 'blue'])
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color = values, node_size = 5000, cmap=cmap)
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
    output = BytesIO()
    plt.savefig(output) 
    output.seek(0)
    plt.clf()
    return Response(output.getvalue(), mimetype='image/png')


if __name__ == "__main__":
    app.run()
