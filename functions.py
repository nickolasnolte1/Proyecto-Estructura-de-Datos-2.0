from typing import NamedTuple
from datetime import datetime

from sympy import lcm_list


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
    username: str
    email: str
    password: str
    interests: list
    posts: LinkedList


def crear_usuario(users, username, email, password):
    interests=[]
    posts=LinkedList()
    a=User(username,email, password, interests, posts)
    users.append(a)
    return users



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




