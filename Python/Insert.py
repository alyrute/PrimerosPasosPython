#insertar datos en SQL

cursorInsert= conexion.cursor()

nombre="Alicia"

consulta = "INSERT INTO persona (nombre, apellido, telefono, edad,  email, sexo) VALUES ('Alicia', 'Garcia', '123456789', 25, 'ali@gmail.com', 'Femenino')"

cursorInsert.execute(consulta)









cursorInsert.commit()
cursorInsert.close()
