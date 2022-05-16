from typing import NamedTuple
from datetime import datetime, timedelta
import json
import re
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt

from numpy import sort



class Notification(NamedTuple):
    notification: str
    dateadded: str 


class Post(NamedTuple):
    dateposted: str
    post: str
    category: str


class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
    def __init__(self):
      self.headval = None

    def listprint(self):
      printval = self.headval
      while printval is not None:
         printval = printval.nextval


class User(NamedTuple):
    id: int
    username: str
    email: str
    password: str
    interests: list

# Queue implementation in Python

class Queue:
    def __init__(self):
        self.queue = []
    # Add an element
    def enqueue(self,dpostinfo, n, dcategory):
        current_time = datetime.now()
        future_time = current_time + timedelta(minutes=int(n))
        future_time_str = future_time.strftime('%m-%d-%Y %H:%M:%S.%f')
        dpostx=Post(future_time_str, dpostinfo, dcategory)
        self.queue.append(dpostx)
        ordenar=self.queue
        ordenar.sort(key=lambda x: x.dateposted)
        self.queue=ordenar

    # Remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)


    # Display  the queue
    def display(self):
        prueba=self.queue
        prueba.sort(key=lambda x: x.dateposted)
        for i in prueba:
            print(f"Date posted:{i.dateposted}")
            print(f"Date posted:{i.post}")
            print(f"Date posted:{i.category}")

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def length(self) -> int:
        return len(self.stack)
  
    def push(self, noti) -> None:
        time=datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')
        x=Notification(noti, time)
        self.x = x
        self.stack.append(x)       

    def pop(self) -> None:
        self.stack.pop()

class Graph():
    def __init__(self):
        self.friends = {}
        self.users = []
        self.edges=[] 

    def graph_node(self, node):
        if node not in self.users:
            self.users.append(node)
        else:
            print("The given node exists")
    
    def graph_edge(self, user1, user2):
        temp = []
        for node in self.users:
            if node.username==user1:
                a=node.username
                for node in self.users:
                    if node.username==user2: 
                        b=node.username
                        if a not in self.friends:
                            temp.append(b)
                            self.friends[a] = temp
                            break
                        elif a in self.friends:
                            temp.extend(self.friends[a])
                            temp.append(b)
                            self.friends[a] = temp
                            break
    
    def disp_graph(self):
        for node in self.friends:
            print(node, " -> ", [i for i in self.friends[node]])
    
    def generate_edges(self):
        for node in self.friends:
            for friend in self.friends[node]:
                self.edges.append((node, friend))
    
        
users=Graph()

b=User(0, "esteban", "estebansamayoa@ufm.edu","12345", ["politica", "programacion"])
c=User(1, "danielbehar", "danielbehar@ufm.edu","diosesmipastor", ["musica", "politica"])
d=User(2, "nickonolte", "nickolasnolte@ufm.edu","bodoque33", ["programacion", "deportes"])
e=User(3, "josereyes", "josereyes@ufm.edu","enano", ["deportes"])
f=User(4, "fernandagonzalez", "fernandagonzalez@ufm.edu","estructurasdedatos", ["programacion", "musica", "politica"])
users.graph_node(b)
users.graph_node(c)
users.graph_node(d)
users.graph_node(e)
users.graph_node(f)
users.graph_edge("esteban","danielbehar")
users.graph_edge("esteban","nickonolte")
users.graph_edge("nickonolte","esteban")
users.graph_edge("nickonolte","josereyes")
users.graph_edge("fernandagonzalez","josereyes")
users.graph_edge("fernandagonzalez","nickonolte")
users.graph_edge("esteban","fernandagonzalez")
users.disp_graph()
users.generate_edges()






postsx=Queue()
postsx.enqueue("Bad Bunny Viene a Guatemala!", 0, "Música")
postsx.enqueue("Guerra de Rusia contra Ucrania!", 0, "Politica")

notifications=Stack()

notifications.push("Welcome to JINX! Sign Up Successful")


def crear_usuario(username, email, password):
    i=len(users.users)
    interests=[]
    a=User(i,username, email, password, interests)
    users.graph_node(a)
    i=len(users.users)
    return users, i 

def agregar_intereses(users,i, interests):
    a=users.users[0]
    for user in users.users:
        if user.id==i-1:
            a=user
        else: 
            continue
    for interes in interests:
        a.interests.append(interes)
    return users, i-1



def printear_informacion(users,i):
    a=users.users[0]
    for user in users.users:
        if user.id==i:
            a=user
        else: 
            continue
    username=a.username
    email =a.email
    password=a.password
    interests=a.interests
    return username, email, password, interests

def printear_posts(postsx):
    postinfo=[]
    current_time = datetime.now()
    current_time = current_time.strftime('%m-%d-%Y %H:%M:%S.%f')
    for i in postsx.queue:
        if i.dateposted<=current_time:
            postinfo.append(i)
    postinfo.sort(key=lambda x: x.dateposted)
    postinfo.reverse()
    return postinfo


def printear_notifications(notifications):
    notifs=[]
    for i in notifications.stack:
        name=i.notification
        date=i.dateadded
        notifs.append([name, date])
    notifs.reverse()
    return notifs


#Email validator
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        print("")
 
    else:
        print("Invalid Email")




