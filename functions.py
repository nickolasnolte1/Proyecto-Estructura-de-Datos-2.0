from platform import node
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



class User(NamedTuple):
    id: int
    username: str
    email: str
    password: str
    interests: list




class Heap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0
 
    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
 
    def insert(self, post, category, minutes):
        current_time = datetime.now()
        future_time = current_time + timedelta(minutes=int(minutes))
        future_time_str = future_time.strftime('%m-%d-%Y %H:%M:%S.%f')
        k=Post(future_time_str, post, category)
        self.heap_list.append(k)
        self.current_size += 1
        self.sift_up(self.current_size)
 
    def sift_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc
 
    def min_child(self, i):
        if (i * 2)+1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i * 2
            else:
                return (i * 2) + 1

    def get_min(self):
        if len(self.heap_list) == 0:
            return 'Empty heap'
        root = self.heap_list[1]
        return root
 
    def delete_min(self):
        if len(self.heap_list) == 0:
            return 'Empty heap'
        root = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        *self.heap_list, _ = self.heap_list
        self.current_size -= 1
        self.sift_down(1)
        return root



postsx = Heap()
postsx.insert("Python es un gran lenguaje de programación!", "Programación",0)
postsx.insert("Ya vienen las elecciones de Guatemala!", "Politíca",-2)
postsx.insert("Bad Bunny viene a Guatemala!", "Musica",20)
postsx.insert("Doctor Strange In the Multiverse of Madness is Out!", "Peliculas", -10)
postsx.insert("Ya salió el trailer de Thor Love and Thunder!", "Peliculas", 5)






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

    def search_user(self, start_user, key):
        visited = []
        queue = []     
        visited.append(start_user)
        queue.append(start_user)
        while queue:
            s = queue.pop(0) 
            # print (s, end = " ") 
            if s==key:
                return s
            for neighbour in self.friends[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return None

    
        
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
# users.disp_graph()
users.generate_edges()
userprueba=users.search_user("fernandagonzalez","josereyes")
print(userprueba)




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
    currenttime=datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')
    while (1):
        node=postsx.get_min()
        print(node)
        if node.dateposted<=currenttime:
            postinfo.append(node)
            postsx.delete_min()
        elif node.dateposted>=currenttime:
            break
        else: 
            continue
    postinfo.reverse() 
    return postinfo


def updatear_posts(postsx, postinfo):
    postinfo.sort(key=lambda x: x.dateposted)
    currenttime=datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')
    while (1):
        node=postsx.get_min()
        print(node)
        if node.dateposted<=currenttime:
            postinfo.append(node)
            postsx.delete_min()
        elif node.dateposted>=currenttime:
            break
        else: 
            continue
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



