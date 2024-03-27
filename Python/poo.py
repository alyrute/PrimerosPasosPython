

class Persona:
    nombre = ""
    apellidos = ""
    telefono = ""
    edad = ""
    email = ""
    id = ""
    sexo = ""

    def __init__(self, nombrey, apellidos, id):
        self.nombre = nombrey
        self.apellidos = apellidos
        self.id = id
       



    def saludar(self):
        saludo= "Hola, mi nombre es : " + self.nombre + " " + self.apellidos + " mi id es: " + self.id
        return saludo
    





class planilla(Persona):
    salario=15000
    moneda= "Euros"
    

    def misalario(self):
        msj= "mi salario es de " +  str(self.salario) + " " + self.moneda
        return msj
    





p1 = planilla("Alicia", "Ruiz", "5")
p2 = Persona("Juan", "Perez", "6")

print (p1.saludar())
print (p1.misalario())
print (p2.saludar())


