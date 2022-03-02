from typing import NamedTuple
from datetime import datetime
import json



users=[]
i=0

class Post(NamedTuple):
    datecreated: str
    post: str


class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
   def __init__(self):
      self.headval = None

class User(NamedTuple):
    id: int
    username: str
    email: str
    password: str
    interests: list
    posts: LinkedList


def crear_usuario(username,i, email, password):
    posts=LinkedList()
    interests=[]
    a=User(i,username, email, password, interests, posts)
    i+=1
    users.append(a)
    return users, i-1

def agregar_intereses(users, i, interests):
    a=users[i]
    print(a.interests)
    for interes in interests:
        a.interests.append(interes)
    print(a)
    return users, i

def agregar_post(users, i, post):
    a=Post(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), post)
    list1=users[i].posts
    node=Node(a)
    list1.headval.nextval=node
    return users, i

def printear_informacion(users,i):
    user=users[i]
    username=user.username
    email =user.email
    password=user.password
    interests=user.interests
    return username, email, password, interests






# post1=Post(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), "Hola")
# post2=Post(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), "Adios")
# list1 = LinkedList()
# list1.headval = Node(post1)
# e2 = Node(post2)
# list1.headval.nextval = e2

# user1=User('esteban','estebansamayoa@ufm.edu', '1234', ['Sports', 'Movies'], list1)


# print('USER:\n')
# print('______________________________\n')
# print(f'Username:{user1.username}\n')
# print(f'Email:{user1.email}\n')
# print(f'Password:{user1.password}\n')
# print('______________________________\n')
# print('Interests:\n')
# for i in user1.interests:
#     print(i)
# print('______________________________\n')
# print('______________________________\n')
# print('Posts:\n')
# printval = user1.posts.headval
# while printval is not None:
#     print('______________________________\n')
#     print(printval.dataval.post)
#     print('______________________________\n')
#     print(f'Date posted:{printval.dataval.datecreated}')
#     printval = printval.nextval




