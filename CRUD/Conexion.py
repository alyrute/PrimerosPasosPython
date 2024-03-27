#pip intall mysql-connector-phyton

import mysql.connector


class Cconexion:
    def ConexionBaseDatos():
        try:
            conexion = mysql.connector.connect(user='ali',
                                               password='ali1',
                                               host='127.0.0.1',
                                               database='bbddprueba',
                                               port='3306'
                                               )
            print("Conexion correcta" )
            return conexion
            
            
            
        except mysql.connector.Error as error:
            print("Error al conectase a la BBDD")
            return conexion
        
    ConexionBaseDatos()