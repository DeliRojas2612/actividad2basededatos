
class Persona():
    def __init__(self):
        self.personas = {}

    def agregarPersonas(self):
        self.codigo = input("Codigo: ")
        if self.codigo in self.personas:
            print("Este codigo ya existe.")
        else:
            self.nombre = input("Nombre: ")
            self.edad = input("Edad: ")
            self.personas[self.codigo] = (self.nombre, self.edad)

    def eliminarPersonas(self):
        if len(self.personas) == 0:
            print("No hay nada para eliminar.")
        else:
            self.cod = input("Ingrese el codigo de la persona que desea eliminar => ")
            if (self.cod in self.personas):
                print(f"Se eliminó {self.personas.pop(self.cod)}")
            else:
                print("Este codigo no existe")

    def mostrarPersonas(self):
        if len(self.personas) == 0:
            print("La lista está vacia")
        else:
            for i, v in self.personas.items():
                print(f"{i}: {v}")


class Empleado(Persona):
    def __init__(self):
        super().__init__()

    def agregarEmpleado(self):
        super().agregarPersonas()
        if (self.codigo in self.personas) == False:
            self.salario = float(input("Salario: "))
            self.personas[self.codigo] = (self.nombre, self.edad, self.salario)


    def eliminarEmpleado(self):
        super().eliminarPersonas()

    def mostrarEmpleado(self):
        super().mostrarPersonas()


def menu():
    p1 = Persona()
    e1 = Empleado()
    menu = 0
    while menu != 7:

        print("\nMENÚ")
        print("1. Agregar Persona")
        print("2. Eliminar Persona")
        print("3. Mostrar Persona")
        print("4. Agregar Empleado")
        print("5. Eliminar Empleado")
        print("6. Mostrar Empleado")
        print("7. Salir")
        menu = int(input("Ingrese opción => "))

        if menu == 1:
            continua = "s"
            while continua == "s":
                print("Agregar Persona")
                p1.agregarPersonas()
                continua = input("Desea continuar agregando s/n: ")
                continua = continua.lower()
        elif menu == 2:
            continua = "s"
            while continua == "s":
                print("Eliminar Persona")
                p1.eliminarPersonas()
                continua = input("Desea continuar eliminando s/n: ")
                continua = continua.lower()
        elif menu == 3:
            p1.mostrarPersonas()
        elif menu == 4:
            continua = "s"
            while continua == "s":
                print("Agregar Empleado")
                e1.agregarEmpleado()
                continua = input("Desea continuar agregando s/n: ")
                continua = continua.lower()
        elif menu == 5:
            continua = "s"
            while continua == "s":
                print("Eliminar Empleado")
                e1.eliminarEmpleado()
                continua = input("Desea continuar eliminando s/n: ")
                continua = continua.lower()
        elif menu == 6:
            e1.mostrarEmpleado()
        elif menu == 7:
            print("Finalizado")
        else:
            print("Esta opción no existe")


def inicio():
    menu()


if __name__ == "__main__":
    inicio()