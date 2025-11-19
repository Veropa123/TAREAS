import json

ARCHIVO = "estudiantes.json"

#----------------------CARGAR ESTUDIANTES--------------

def leer_datos():
    """Carga los estudiantes desde el archivo JSON."""

    try:
        with open(ARCHIVO,"r") as f:
            # json.load convierte el texto JSON a una lista de Python
            datos_cargados = json.load(f) # CORREGIDO: Almacenar y devolver el resultado de load()
            return datos_cargados
            
    except FileNotFoundError:
        # Si el archivo no existe, devuelve una lista vacía
        return []
    except json.JSONDecodeError:
        # Si el archivo existe pero esta vacio o mal formado
        print("Advertencia: El archivo JSON está vacío o mal formado.")
        return []

#------------------GUARDAR DATOS EXISTENTES------------------

def guardar_datos(estudiantes):
   """Escribe una lista actualizada de los estudiantes en el archivo JSON."""
   with open(ARCHIVO,"w") as f:
      # json.dump convierte la lista de python a texto JSON y los guarda
      json.dump(estudiantes, f, indent=4)

#-----------------CREAR O AÑADIR-------------------------------

def crear_estudiantes(nombre, edad, curso): # CORREGIDO: Sintaxis de función
    """Añade un nuevo estudiante con validación"""
    
    # Leer los datos existentes
    estudiantes = leer_datos()
   
    # Determinar el nuevo ID (el ID más alto + 1)
    # si la lista está vacía, el ID inicial es 1.
    nuevo_id = max([e["id"] for e in estudiantes], default= 0) + 1
   
    # Crear el nuevo objeto (diccionario) usando los argumentos de entrada (nombre, edad, curso)
    nuevo = {
        "id": nuevo_id,
        "nombre": nombre,
        "edad": edad,
        "curso": curso,
    }
   
    # añadir a la lista y guardar
    estudiantes.append(nuevo)
    guardar_datos(estudiantes)
    print(f"Estudiante '{nombre}' (ID:{nuevo_id}) creado exitosamente.")

    

#-----------------PREGUNTAR DATOS AL USUARIO-------------------

def preguntar_datos():
    """Pregunta al usuario los datos del nuevo estudiante y los guarda."""
    
    # 1. Solicitar el nombre 
    nombre_nuevo = input("   > Nombre del estudiante: ")
    
    # 2. Solicitar la edad (y convertir a número entero)
    while True:
        try:
            edad_str = input("   > Edad: ")
            edad_nueva = int(edad_str)
            break
        except ValueError:
            print("Error: La edad debe ser un número entero. Inténtalo de nuevo.")
            
    # 3. Solicitar el curso 
    curso_nuevo = input("   > Curso: ")
    
    # 4. Llamar a la función que guarda los datos
    crear_estudiantes(nombre_nuevo, edad_nueva, curso_nuevo)

    #-----------------MOSTRAR TODOS LOS ESTUDIANTES----------------

def mostrar_estudiantes_actuales():
    """Lee y muestra en la consola la lista completa de estudiantes."""
    
    estudiantes = leer_datos()
    
    if not estudiantes:
        print("\n[INFO] La lista de estudiantes está vacía.")
        return

    print("\n--- ARCHIVO JSON DE ESTUDIANTES (ACTUALIZADO) ---")
    for e in estudiantes:
        print(f"ID: {e['id']} | Nombre: {e['nombre']} | Edad: {e['edad']} | Curso: {e['curso']}")
    print("--------------------------------------------------")

# --- REEMPLAZA TODA LA SECCIÓN DE EJECUCIÓN CON ESTO ---

def ejecutar_programa():
    print("\n====================================")
    print("     GESTOR DE ESTUDIANTES JSON")
    print("====================================")

    while True:
        # Preguntamos si el usuario quiere seguir o salir
        opcion = input("\nPulsa [Enter] para añadir un estudiante, o escribe [0] para salir: ")
        
        if opcion == '0':
            print("\n👋 ¡Gracias por usar el gestor! Guardando y saliendo.")
            break  # Rompe el bucle while True, terminando el programa
        
        # Si no es '0', llamamos a la función para pedir y guardar el estudiante
        preguntar_datos()
        
        # Opcional: Mostramos la lista completa después de cada adición
        mostrar_estudiantes_actuales() 
        

# --- Asegúrate de que esta línea es la última en el archivo ---
ejecutar_programa()

