import json

ARCHIVO = "estudiantes.json"

#contenido de app.py
#----------------------CARGAR ESTUDIANTES--------------


def leer_datos():
    """Carga los estudiantes desde el archivo JSON."""

    try:
        
        with open(ARCHIVO,"r") as f:
            #json.load convierte el texto JSON a una lista de Python

         return json.load(f)
    except FileExistsError:
        #Si el archivo no existe, devuelve una lista vacia
        return[]
    except json.JSONDecodeError:
        #Si el archivo existe pero esta vacio o mal formado

      print("Advertencia: El archivo JSON esta vacio")
    return[]

#------------------GUARDAR DATOS EXISTENTES------------------

def guardar_datos(estudiantes):
   """Escribe una lista actualizada de los estudiantes desde el archivo JSON."""
   with open(ARCHIVO,"w") as f:
      #json.dump convierte la lista de python a texto JSON y los guarda
      json.dump(estudiantes,f,indent=4)

#-----------------CREAR O AÑADIR-------------------------------

def crear_estudiantes(nombre,edad,curso):
   """Añade un nuevo estudiante con validación"""

   #Leer los datos existentes

   estudiantes = leer_datos()

   #Determinar el nuevo ID(el ID mas alto + 1)
   # si la lista esta vacia, el ID inicial es 1.

nuevo_id = max

