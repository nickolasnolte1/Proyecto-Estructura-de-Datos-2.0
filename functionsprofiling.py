import cProfile
import functions


#Aqui se agrega un post al Queue para ordenarlo despues por fecha y hora
cProfile.run('functions.postsx.insert("Prueba de Profiling!", "Politica", 0)')
#Aqui se elimina el post con la fecha más nueva que sea igual o menor a la fecha y hora actual
#Aqui se agrega una notificación a la Stack de notificaciones
cProfile.run('functions.notifications.push("Message sent correctly!")')
#Aqui se eliminar la primera notificación a la Stack de notificaciones
cProfile.run('functions.notifications.pop()')
#Aquí se llama la función que ordena las notificaciones para imprimirlas
cProfile.run('functions.printear_notifications(functions.notifications)')