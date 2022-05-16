from flask import Flask, render_template, request, url_for, redirect, flash, Response
from flask.wrappers import Request
from functions import crear_usuario, printear_notifications, printear_posts, users, agregar_intereses, printear_informacion, postsx, check, notifications
import flask_profiler
import re
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO


#para verificar el formato del email. 
regex = r'\b[A-Za-z0-9_%+-.]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['flask_profiler'] = {
    "enabled" : app.config['DEBUG'],
    "storage" : {
        "engine" : "sqlite"
    },
    "basicAuth" : {
        "enabled" : True,
        "username" : "admin",
        "password" : "admin"
    },
    "ignore": [
	    "^/static/.*"
	]

}
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

flask_profiler.init_app(app)

def check(email):

	if(re.fullmatch(regex, email)):
		return "Valid Email"

	else:
		return "Invalid Email"


@app.route('/notifications')
def noti():
    return render_template('notifications.html')

@app.route('/' , methods = ["GET", "POST"])
@flask_profiler.profile()
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
    print(users.users)
    return render_template('signup.html')

@app.route('/categories/<user_id>', methods = ["GET", "POST"])
@flask_profiler.profile()
def categories(user_id):
    if request.method == 'POST':
        interests=request.form.getlist('check')
        if (len(interests)>0):
            a, user_id=agregar_intereses(users, int(user_id), interests)
            return redirect(url_for('home', user_id=user_id))
    return render_template('categories.html')


@app.route('/homepage/<user_id>', methods = ["GET", "POST"])
@flask_profiler.profile()
def home(user_id):
    username, email, password, interests=printear_informacion(users,int(user_id))
    postinfo=printear_posts(postsx)
    notifs=printear_notifications(notifications)
    if request.method == 'POST':
        if request.form['btn']=='Accept':
            friend="danielbehar"
            print(f"EL USERNAME DEL AMIGO ES:{friend}")
            users.graph_edge(username, friend)
            users.disp_graph()
            users.generate_edges()
        if request.form['btn']=='post':
            post=request.form.get("post23")
            category=request.form.get('categories')
            minutes=request.form.get('datetopost')
            print(post)
            print(category)
            postsx.enqueue(post, minutes, category)
            if int(minutes)>0:
                notifications.push(f"Post will be published in {minutes} minutes.")
            else:
                notifications.push("Post was published Successfully!")
            postinfo=printear_posts(postsx)
            notifs=printear_notifications(notifications)
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
