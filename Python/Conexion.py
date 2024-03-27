# conexion bbdd


import mysql.connector

server= 'localhost'
port = '3306'
bd = 'bbddprueba'
usuario = 'ali'
contrasena = 'ali1'

try:
    conexion = mysql.connector.connect(
        host=server,
        port=port,
        database=bd,
        user=usuario,
        password=contrasena)
    
    if conexion.is_connected():
        print("Conexión exitosa")
      
        
except Exception as e:
    print("Error en la conexion")
    print(e)
    
    
cursor = conexion.cursor()
cursor.execute("SELECT * FROM persona")


# Definir la función consulta
def consulta(conexion, query):
    cursor = conexion.cursor()
    cursor.execute(query)
    return cursor.fetchall()


"""personas = cursor.fetchone()
while personas:
    print(personas[2])
    personas = cursor.fetchone()"""
    
    
personas = cursor.fetchall()
for persona in personas:
    print(persona)


cursor.close()


"""
cursorInsert= conexion.cursor()

nombre="Alicia"

consulta = "INSERT INTO persona (nombre, apellido, telefono, edad,  email, sexo) VALUES ('Alicia', 'Garcia', '123456789', 25, 'ali@gmail.com', 'Femenino')"

cursorInsert.execute(consulta)









conexion.commit()
cursorInsert.close()

"""

# Actualizar informacion

cursorUpdate = conexion.cursor()

consulta = "UPDATE persona SET nombre = %s WHERE id = %s"

cursorUpdate.execute(consulta, ('Thiago','8'))   

conexion.commit()
cursorUpdate.close()



#Eliminar datos

cursorEliminar = conexion.cursor()
consulta= "DELETE FROM persona WHERE id = %s"
cursorEliminar.execute(consulta, ('4',))

conexion.commit()
cursorEliminar.close()

