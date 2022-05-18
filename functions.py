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
        self.print_list=[]
 
    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2
 
    def insert(self, post, category, minutes):
        current_time = datetime.now()
        future_time = current_time + timedelta(minutes=int(minutes))
        future_time_str = future_time.strftime('%m-%d-%Y %H:%M:%S')
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
            if s==key:
                return s
            for neighbour in self.friends[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return None

    
        
users=Graph()

b=User(0, "esteban", "estebansamayoa@ufm.edu","12345", [])
c=User(1, "danielbehar", "danielbehar@ufm.edu","diosesmipastor", ["musica", "politica"])
d=User(2, "nickonolte", "nickolasnolte@ufm.edu","bodoque33", ["programacion", "deportes"])
e=User(3, "josereyes", "josereyes@ufm.edu","enano", ["deportes"])
f=User(4, "fernandagonzalez", "fernandagonzalez@ufm.edu","estructurasdedatos", ["programacion", "musica", "peliculas"])
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
users.graph_edge("josereyes","fernandagonzalez")
users.graph_edge("danielbehar","nickonolte")
# users.disp_graph()
users.generate_edges()






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


def BinarySearch(users, user_id):
    first = 0
    last = len(users.users)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if users.users[mid].id == user_id:
            index = mid
        else:
            if user_id<users.users[mid].id:
                last = mid -1
            else:
                first = mid +1
    username=users.users[index].username
    email=users.users[index].email
    password=users.users[index].password
    interests=users.users[index].interests
    return username, email, password, interests



def info_username(users, username):
    a=users.users[0]
    for user in users.users:
        if user.username==username:
            a=user
        else: 
            continue
    username=a.username
    email =a.email
    interests=a.interests
    return username, email, interests



def printear_posts(postsx):
    currenttime=datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')
    while (1):
        node=postsx.get_min()
        if node.dateposted<=currenttime:
            lis=postsx.print_list
            lis.append(node)
            postsx.delete_min()
            lis.sort(key=lambda x: x.dateposted)
            lis.reverse()
            postsx.print_list=lis
        elif node.dateposted>=currenttime:
            break
        else: 
            continue 
    return postsx.print_list


def updatear_posts(postsx):
    currenttime=datetime.now().strftime('%m-%d-%Y %H:%M:%S.%f')
    while (1):
        node=postsx.get_min()
        print(node)
        if node.dateposted<=currenttime:
            lis=postsx.print_list
            lis.append(node)
            postsx.delete_min()
            lis.sort(key=lambda x: x.dateposted)
            lis.reverse()
            postsx.print_list=lis
        elif node.dateposted>=currenttime:
            break
        else: 
            continue
     
    return postsx.print_list


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



