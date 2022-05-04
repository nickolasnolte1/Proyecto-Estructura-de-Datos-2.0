from typing import NamedTuple
from datetime import datetime, timedelta
import json
import re

from numpy import sort


users=[]
i=0

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
         print (printval.dataval)
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






postsx=Queue()
postsx.enqueue("Bad Bunny Viene a Guatemala!", 0, "Música")
postsx.enqueue("Guerra de Rusia contra Ucrania!", 0, "Politica")

notifications=Stack()

notifications.push("Welcome to JINX! Sign Up Successful")

b=User(0, "esteban", "estebansamayoa@ufm.edu","12345", ["politica", "programacion"])
users.append(b)

def crear_usuario(username,i, email, password):
    interests=[]
    a=User(i,username, email, password, interests)
    i+=1
    users.append(a)
    return users, i 

def agregar_intereses(users, i, interests):
    a=users[i]
    print(a.interests)
    for interes in interests:
        a.interests.append(interes)
    print(a)
    return users, i



# def agregar_post(postsx,post, category, n):
#     todaydate=datetime.today()
#     a=Post(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), post, category)
#     node=Node(a)
#     if postsx.headval is None:
#         postsx.headval = node
#         return postsx
#     laste = postsx.headval
#     while(laste.nextval):
#         laste = laste.nextval
#     laste.nextval=node
#     return postsx

def printear_informacion(users,i):
    user=users[i]
    username=user.username
    email =user.email
    password=user.password
    interests=user.interests
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
    print(postinfo)
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


