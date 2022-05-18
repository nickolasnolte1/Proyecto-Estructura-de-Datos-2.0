# JINX
<img width="435" alt="image" src="https://user-images.githubusercontent.com/61555652/156282205-f4f177da-ecc2-4387-97a9-9c743c38f15a.png">


## Proyecto de Estructuras de Datos creado en Python y HTML/CSS
**Creado por:**
- Esteban Samayoa
- Nickolas Nolte



## Descripción de la aplicación:
 
**Jinx es una red social donde los usuarios crearán una cuenta, un perfil y podrán publicar en un feed sus pensamientos, ideas, temas de discusión, etc. La idea es que las personas puedan interactuar y expresarse libremente por medio de texto.**



## La aplicación cuenta con las siguientes funcionalidades:

*   Crear un perfil a través de la página de Signup
    * Username
    * Correo
    * Contraseña 
    * Confirmar la contraseña


*   Elegir los temas que más le interesan al usuario. Puede elegir entre:
    * Política 
    * Cine 
    * Deportes
    * Música
    * Arte
    * Programación

* Realizar posts en la página de feed
* Ver posts realizados anteriormente.
* Programar tiempos para realizar un post
* Ver notificaciones de la página
* Agregar amigos
* Bucsar información de amigos


#### ⚠️ **PARA PODER CORRER EL PROGRAMA, SE DEBE CORRER EL SIGUIENTE COMANDO EN LA TERMINAL:**

`pip3 install flask-profiler`

####  Y DESPUES SE DEBE CORRER EL ARCHIVO DE PYTHON LLAMADO **[app.py](app.py)** 



# Diagrama de casos de uso
<img width="705" alt="image" src="https://user-images.githubusercontent.com/61555652/168938429-4fe39924-d9e4-40fd-b9e6-37c1d8e67498.png">

# Grafos

<img width="1347" alt="image" src="https://user-images.githubusercontent.com/61555652/168939331-eb2d421d-ab4e-4e96-bade-0050f8d603c2.png">


# Profiling

Se utilizó "Flask Profiler" como herramienta para hacer el profiling del API.

A continuación se adjunta una imagen del profiling.

<img width="966" alt="image" src="https://user-images.githubusercontent.com/61555652/156972756-ba80b2b5-9229-43bc-a925-4ad1e48eacea.png">

Tambien se utilizó cProfile para hacer profiling de las funciones que utiliza el programa. Estas se encuentran dentro de un archivo llamado functionsprofiling.py 




# Unit Testing 

Se realizaron 6 unit tests para probar las diferentes funciones.
Estos tests se pueden encontrar en el documento llamada "testing.py"

# Documento de Product Spec.
https://docs.google.com/document/d/1F9c-QuyvVXn5SGp9ML6XHyUR90SC4buGXuOyTreqIgU/edit?usp=sharing
