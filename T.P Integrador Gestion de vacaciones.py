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
            dias = int(input("Ingrese la cantidad de días que desea solicitar: "))

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

def buscar_empleado(empleados, dni):

    if dni in empleados:
        return empleados[dni]

    return None

def solicitar_vacaciones(empleado):

    try:
        dias_solicitados = int(
            input("Ingrese la cantidad de días que desea solicitar: ")
        )

        if dias_solicitados <= 0:
            print("Debe ingresar una cantidad mayor a 0.")

        elif dias_solicitados <= empleado["dias"]:
            print("Solicitud aprobada.")
            print("Vacaciones registradas correctamente.")

        else:
            print("Solicitud rechazada.")
            print("No posee días suficientes.")

    except ValueError:
        print("Error: Debe ingresar un número entero."

#Programa Principal
empleados = cargar_empleados() #Carga la lista de empleados

while True: #Menu Interactivo

    print("CHATBOT DE GESTIÓN DE VACACIONES")
    print("1. Solicitar vacaciones")
    print("2. Salir")

    opcion = input("Seleccione una opción: ") #Pide una opción del menú

    if opcion == "1": 
        dni = validar_dni() #Verifica y busca la identidad del empleado
        empleado = buscar_empleado(empleados, dni)

        if empleado:
            print(f"Nombre: {empleado['nombre']}") #Muestra los datos del empleado
            print(f"Días disponibles: {empleado['dias']}")
            solicitar_vacaciones(empleado) #Solicita las vacaciones

        else:
            print("Error: Empleado no encontrado.") #Muestra por pantalla que el empleado no está registrado

    elif opcion == "2":
        print("Gracias por utilizar el sistema.") #Cierra el programa
        break

    else:
        print("Error: Opción inválida.")
