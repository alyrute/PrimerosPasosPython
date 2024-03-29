from Conexion import * 

class Cclientes:
    @staticmethod
    def ingresarCliente(nombre, apellido, telefono, edad, email, sexo):
        try:
            cone= Cconexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql= "insert into persona value(null, %s, %s, %s, %s, %s, %s);"
            
            #Variable Valores tiene que ser una tupla
            #Como minima expresion es: (valor, ) la coma hace que sea una tupla
            #Las tuplas son Lista inmutables, eso quiere decir que no se modifica. 
            valores= (nombre, apellido, telefono, edad, email, sexo)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro ingresado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso de datossssssssssssss")
            
    def mostrarClientes():
       
        try:
            cone= Cconexion.ConexionBaseDatos()
            cursor = cone.cursor()
            cursor.execute("SELECT * FROM persona")
            rows = cursor.fetchall()
            cone.close()
            return rows
        except Exception as error:
            print("Error al mostrar los clientes:::::: {error}")
            return []
        
    def modificarCliente( id,nombre, apellido, telefono, edad, email, sexo):
        try:
            cone= Cconexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql= "update persona set persona.nombre=%s , persona.apellido=%s ,persona.telefono=%s ,  persona.edad=%s , persona.email=%s ,persona.sexo=%s where persona.id=%s";
            valores= (nombre, apellido, telefono, edad, email, sexo, id)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Actualizado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de actualizacion de datossssssssssssss")
    
    def eliminarCliente( id,nombre, apellido, telefono, edad, email, sexo):
        try:
            cone= Cconexion.ConexionBaseDatos()
            cursor = cone.cursor()
            sql= "update persona set persona.nombre=%s , persona.apellido=%s ,persona.telefono=%s ,  persona.edad=%s , persona.email=%s ,persona.sexo=%s where persona.id=%s";
            valores= (nombre, apellido, telefono, edad, email, sexo, id)
            cursor.execute(sql, valores)
            cone.commit()
            print(cursor.rowcount, "Registro Actualizado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de actualizacion de datossssssssssssss")
            