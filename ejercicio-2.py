class Alumno: 
    nombre = ""
    nota = 0
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def info(self):
        return "Nombre: " + self.nombre + ' Nota: ' + str(self.nota)

    def estado(self):
        return "Aprobado: " +  str(self.nota >= 7)


a = Alumno('Agustin', 7)

print(a.info())
print(a.estado())