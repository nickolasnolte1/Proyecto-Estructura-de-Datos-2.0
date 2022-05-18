import unittest
from functions import crear_usuario, agregar_intereses, users, postsx, notifications
from flask import Flask, render_template
from app import app
from datetime import datetime, timedelta

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

    def test_profile(self):
        response = self.client.get("/profile/esteban", data={"username":"esteban"})
        assert response.status_code == 200



class Testprueba(unittest.TestCase):

    def test_crear_user(self):
        id=5
        username="esteban"
        email="estebansamayoa@ufm.edu"
        password="1234"
        users,i =crear_usuario(username, email, password)
        self.assertEqual(username, users.users[5].username)
        self.assertEqual(email, users.users[5].email)
        self.assertEqual(password, users.users[5].password)


    def test_intereses(self):
        intereses=["musica","arte", "deportes"]
        users2, i=agregar_intereses(users, 1, intereses)
        self.assertEqual(intereses, users2.users[i].interests)
    

    def test_crear_post(self):
        postsx.insert("Prueba de Unit Test!", "Politica", -35)
        current_time = datetime.now()
        future_time = current_time + timedelta(minutes=int(-35))
        future_time_str = future_time.strftime('%m-%d-%Y %H:%M:%S')
        self.assertEqual(postsx.heap_list[1].dateposted, future_time_str)
        self.assertEqual(postsx.heap_list[1].post, "Prueba de Unit Test!")
        self.assertEqual(postsx.heap_list[1].category, "Politica")

    def test_agregarnotification(self):
        notification="Message sent correctly!"
        notifications.push(notification)
        self.assertEqual(notification, notifications.stack[1].notification)


    
if __name__ == "__main__":
    unittest.main()