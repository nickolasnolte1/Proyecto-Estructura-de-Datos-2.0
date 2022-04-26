from typing import NamedTuple
from datetime import datetime
import json
import re




users=[]
i=0


class Post(NamedTuple):
    datecreated: str
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


postsx=LinkedList()
post1=Post(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), "Bad bunny viene a Guatemala!", "musica")
a=Node(post1)
postsx.headval=a

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



def agregar_post(postsx,post, category):
    a=Post(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), post, category)
    node=Node(a)
    if postsx.headval is None:
        postsx.headval = node
        return postsx
    laste = postsx.headval
    while(laste.nextval):
        laste = laste.nextval
    laste.nextval=node
    return postsx

def printear_informacion(users,i):
    user=users[i]
    username=user.username
    email =user.email
    password=user.password
    interests=user.interests
    return username, email, password, interests

def printear_posts(postsx):
    postinfo=[]
    printval = postsx.headval
    while printval is not None:
        postinfo.insert(0,[printval.dataval.post, printval.dataval.datecreated, printval.dataval.category])
        printval = printval.nextval
    return postinfo

#Email validator
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        print("")
 
    else:
        print("Invalid Email")
