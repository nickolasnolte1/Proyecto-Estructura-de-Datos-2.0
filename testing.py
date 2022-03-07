import unittest
import functions
from flask import Flask, render_template
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_signup(self):
        response = self.client.post("/", data={"username": "estebansamayoa", "email":"estebansamayoa@ufm.edu", "password": "1234", "confirm":"1234"})
        assert response.status_code == 200

    def test_home(self):
        response = self.client.get("/homepage/0", data={"user_id":0})
        assert response.status_code == 200
    
    def test_categories(self):
        response = self.client.post("/categories/0", data={"categories":["arte", "musica"]})
        assert response.status_code == 200

class Testprueba(unittest.TestCase):

    def test_crear_user(self):
        id=1
        username="esteban"
        email="estebansamayoa@ufm.edu"
        password="1234"
        users,i =functions.crear_usuario(username, id, email, password)
        self.assertEqual(username, users[i].username)
        self.assertEqual(email, users[i].email)
        self.assertEqual(password, users[i].password)


    def test_intereses(self):
        intereses=["politica","arte", "deportes"]
        users2, i=functions.agregar_intereses(functions.users, 1, intereses)
        self.assertEqual(intereses, users2[i].interests)

    def test_crear_post(self):
        post="Python es un lenguaje de programación"
        category="programacion"
        posts2x=functions.agregar_post(functions.postsx,post, category)
        


if __name__ == "__main__":
    unittest.main()