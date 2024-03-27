import  mysql.connector

conexion = mysql.connector.connect(user='root', 
                                    host='localhost', 
                                    database='bbddprueba',
                                    port='3306')


print(conexion)