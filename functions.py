from typing import NamedTuple


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



list1 = LinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2


