#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)



separador(1)

ingreso = float(input("Ingresa el ingreso anual: "))

if ingreso <= 85528:
    impuesto = round((ingreso * 0.18) - 556.02)
else:
    impuesto = round(14839.02 + (ingreso - 85528) * 0.32)

if impuesto < 0:
    impuesto = 0

print(f"El impuesto calculado es: {impuesto} pesos")

separador(2)

ano = int(input("Ingresa un año: "))

if ano >= 1582:
    
    if (ano % 4 != 0) or ((ano % 100 == 0) and (ano % 400 != 0)):
        print("Año Común")
    else:
        print("Año Bisiesto")
else:
    print("No dentro del período del calendario Gregoriano")

separador(3)

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

user_number = int(input("digues un numero: "))

while user_number != secret_number:
    print("ho has fet malament ets tonto")
    user_number = int(input("torna-ho a intentar: "))
else:
    user_number == secret_number
    print("molt be bro")

     
separador(4)

numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

separador(5)

edad = int(input("Ingrese su edad: "))
ingresos_mensuales = float(input("Ingrese sus ingresos mensuales: "))

if edad > 16 and ingresos_mensuales >= 1000:
    print("vosté pot tributar")
else:
    print("vosté no pot tributar")


separador(6)

sexe = input("Ingrese su sexo (M/F): ")
primera_lletra = input("Ingrese la primera letra de su nombre: ")

if sexe == "F":
    if primera_lletra < "M":
        grupo = "A"
    else: 
        grupo = "B"
else:
    if primera_lletra > "N":
        grupo = "A"
    else:
        grupo = "B"

print(f"Tu grupo és el {grupo}")

separador(7)

renta_anual = float(input("Escribe tu renta anual: "))

if renta_anual < 10000:
        tipo_impositivo = "5%"
if 10000 <= renta_anual < 20000:
        tipo_impositivo = "15%"
if 20000 <= renta_anual < 35000:
        tipo_impositivo = "20%"
if 35000 <= renta_anual < 60000:
        tipo_impositivo = "30%"
if renta_anual > 60000:
        tipo_impositivo = "45%"

print(f"tu renta anual es de {renta_anual} y tu impostivo es de {tipo_impositivo}")

separador(8)

puntuacion = float(input("Ingresa la puntuación del empleado: "))

if puntuacion == 0.0:
    nivel = "Inaceptable"
    cantidad_dinero = 0
elif puntuacion == 0.4:
    nivel = "Aceptable"
    cantidad_dinero = 2400 * puntuacion
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    cantidad_dinero = 2400 * puntuacion
else:
    nivel = "Valor de puntuación inválido"
    cantidad_dinero = 0

if nivel != "Valor de puntuación inválido":
    print(f"El nivel de rendimiento del empleado es '{nivel}' y ganará {cantidad_dinero}€.")
else:
    print("La puntuación ingresada no es válida.")

separador(9)

edad = int(input("ingrese su edad: "))

if edad < 4:
      precio = 0
elif  4 <= edad <= 18:
      precio = 5
else:
      precio = 10

print(f"debes de pagar {precio}€")

separador(10)

vegetariana = input("vols una pizza vegentariana? s/n ")


if vegetariana == "n":
    print("los ingredientes para escoger són: Peperoni, Jamón y Salmón")
else:
    print("los ingredientes para escoger són: Pimiento y tofu")

extra = input("quin ingredient vols? ")

print(f"la teva pizza té tomate, mozzarela i {extra}")

separador(11)

primer_octeto = int(input("Dime el primer octeto: "))
segundo_octeto = int(input("Dime el segundo octeto: "))
tercer_octeto = int(input("Dime el tercer octeto: "))
cuarto_octeto = int(input("Dime el cuarto octeto: "))

clase = ""
tipo = ""

while 0 <= primer_octeto <= 224:
    if 1 <= primer_octeto <= 126:
        clase = "A"
    elif 128 <= primer_octeto <= 191:
        clase = "B"
    elif 192 <= primer_octeto <= 223:
        clase = "C"
    else:
        clase = "Eso no es una IP válida"
        break

    if primer_octeto == 10:
        tipo = "Privada"
        break

    if primer_octeto == 172 and 16 <= segundo_octeto <= 31:
        tipo = "Privada"
        break

    if primer_octeto == 192 and segundo_octeto == 168:
        tipo = "Privada"
        break

    tipo = "Pública"
    break

if clase != "Eso no es una IP válida":
    print(f"Clase: {clase}, Tipo: {tipo}")
else:
    print(clase)