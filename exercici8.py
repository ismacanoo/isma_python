#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)



separador(1)

def tabla_multiplicar():
    num = int(input("Introduce un número entero entre 1 y 10: "))
    if num < 1 or num > 10:
        print("Número fuera de rango.")
        return
    with open(f"tabla-{num}.txt", "w") as file:
        for i in range(1, 11):
            file.write(f"{num} x {i} = {num * i}\n")

tabla_multiplicar()

separador(2)

def mostrar_tabla():
    num = int(input("Introduce un número entero entre 1 y 10: "))
    if num < 1 or num > 10:
        print("Número fuera de rango.")
        return
    try:
        with open(f"tabla-{num}.txt", "r") as file:
            tabla = file.read()
            print(tabla)
    except FileNotFoundError:
        print(f"No existe el fichero tabla-{num}.txt.")

mostrar_tabla()

separador(3)

def mostrar_linea_tabla():
    num = int(input("Introduce un número entero entre 1 y 10: "))
    if num < 1 or num > 10:
        print("Número fuera de rango.")
        return
    try:
        linea = int(input("Introduce el número de línea que deseas ver: "))
        with open(f"tabla-{num}.txt", "r") as file:
            for i, line in enumerate(file, 1):
                if i == linea:
                    print(line.strip())
                    return
            print("Línea no encontrada.")
    except FileNotFoundError:
        print(f"No existe el fichero tabla-{num}.txt.")

mostrar_linea_tabla()

separador(4)

def mostrar_pib_per_capita():
    pais = input("Introduce las iniciales del país (en mayúsculas): ")
    try:
        with open("sdg_08_10.tsv", "r") as file:
            for line in file:
                if pais in line:
                    datos = line.strip().split("\t")
                    print(f"PIB per cápita de {pais}: {datos[1]}")
                    return
        print("País no encontrado en el archivo.")
    except FileNotFoundError:
        print("No se encontró el archivo.")

mostrar_pib_per_capita()

separador(5)

def crear_listin():
    try:
        with open("listin.txt", "x"):
            print("Listín creado correctamente.")
    except FileExistsError:
        print("El listín ya existe.")

def consultar_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    try:
        with open("listin.txt", "r") as file:
            for line in file:
                if nombre in line:
                    datos = line.strip().split(",")
                    print(f"Teléfono de {nombre}: {datos[1]}")
                    return
            print("Cliente no encontrado en el listín.")
    except FileNotFoundError:
        print("No se encontró el listín.")

def añadir_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el teléfono del cliente: ")
    try:
        with open("listin.txt", "a") as file:
            file.write(f"{nombre},{telefono}\n")
        print("Teléfono añadido correctamente.")
    except FileNotFoundError:
        print("No se encontró el listín.")

def eliminar_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    try:
        with open("listin.txt", "r") as file:
            lineas = file.readlines()
        with open("listin.txt", "w") as file:
            for linea in lineas:
                if nombre not in linea:
                    file.write(linea)
        print("Teléfono eliminado correctamente.")
    except FileNotFoundError:
        print("No se encontró el listín.")

while True:
    print("1. Crear listín")
    print("2. Consultar teléfono de un cliente")
    print("3. Añadir teléfono de un nuevo cliente")
    print("4. Eliminar teléfono de un cliente")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        crear_listin()
    elif opcion == "2":
        consultar_telefono()
    elif opcion == "3":
        añadir_telefono()
    elif opcion == "4":
        eliminar_telefono()
    else:
        print("Opción no válida. Inténtalo de nuevo.")

separador(6)

def pedir_usuario_contraseña():
    usuario = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")
    return usuario, contraseña

def registro():
    while True:
        usuario, contraseña = pedir_usuario_contraseña()
        if len(usuario) >= 6 and len(contraseña) >= 8 and any(char.isupper() for char in contraseña) and any(char.islower() for char in contraseña):
            with open("users.txt", "a") as file:
                file.write(f"{usuario},{contraseña}\n")
            print("Usuario registrado correctamente.")
            break
        else:
            print("Usuario o contraseña no válidos. El nombre de usuario debe tener mínimo 6 caracteres y la contraseña mínimo 8 caracteres con al menos una mayúscula y una minúscula.")

def login():
    while True:
        usuario, contraseña = pedir_usuario_contraseña()
        with open("users.txt", "r") as file:
            for line in file:
                stored_usuario, stored_contraseña = line.strip().split(",")
                if usuario == stored_usuario and contraseña == stored_contraseña:
                    print("Estás dentro!")
                    return
        print("Usuario o contraseña incorrectos. Inténtalo de nuevo.")

while True:
    print("1. Registrarse")
    print("2. Login")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        registro()
    elif opcion == "2":
        login()
    else:
        print("Opción no válida. Inténtalo de nuevo.")

