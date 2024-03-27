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
           sql= "select * from persona;"
           resultado=cursor.fetchall()
           cone.commit()
           cone.close()
           return resultado
       except mysql.connector.Error as error:
           print("Error mostrar datos {}".format(error))