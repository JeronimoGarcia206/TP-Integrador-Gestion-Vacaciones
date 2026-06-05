#Funciones de validación 
def validar_dni():
    """Solicita y valida un DNI"""

    while True:

        dni = input("Ingrese su DNI: ").strip()

        if dni.isdigit():
            return dni

        print("Error: El DNI debe contener solo números.")

def validar_dias():
    """Solicita y valida la cantidad de días"""

    while True:

        try:
            dias = int(
                input("Ingrese la cantidad de días que desea solicitar: ")
            )

            if dias > 0:
                return dias

            print("Error: Debe ingresar una cantidad mayor a cero.")

        except ValueError:
            print("Error: Debe ingresar un número entero.")


#Funciones
def cargar_empleados():
    empleados = {}

    with open("empleados.txt", "r", encoding="utf-8") as archivo:

        for linea in archivo:
            dni, nombre, dias = linea.strip().split(",")

            empleados[dni] = {
                "nombre": nombre,
                "dias": int(dias)
            }

    return empleados

#Programa Principal
empleados = cargar_empleados()
