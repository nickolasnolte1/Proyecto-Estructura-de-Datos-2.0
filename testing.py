import unittest
from functions import crear_usuario, agregar_intereses, users, postsx, notifications
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

    def test_post(self):
        response = self.client.post("/homepage/0", data={"post23":"Prueba post!", "categories":"Politica", "datetopost":0})
        assert response.status_code == 200


class Testprueba(unittest.TestCase):

    def test_crear_user(self):
        id=1
        username="esteban"
        email="estebansamayoa@ufm.edu"
        password="1234"
        users,i =crear_usuario(username, id, email, password)
        self.assertEqual(username, users[1].username)
        self.assertEqual(email, users[1].email)
        self.assertEqual(password, users[1].password)


    def test_intereses(self):
        intereses=["politica","arte", "deportes"]
        users2, i=agregar_intereses(users, 1, intereses)
        self.assertEqual(intereses, users2[i].interests)
    

    def test_crear_post(self):
        postsx.enqueue("Prueba de Unit Test!", 0, "Politica")

    def test_agregarnotification(self):
        notifications.push("Message sent correctly!")


    
if __name__ == "__main__":
    unittest.main()