#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(1)

nom = input("Por favor, ingresa tu nombre: ")
print(f"¡Hola \"{nom}\"!")

separador(2)

juan = 3
maria = 5
adan = 6

print(juan, maria, adan, sep=",")
total_manzanas = juan + maria + adan

print("Numero total de pomes:", total_manzanas)

separador(3)

miles = 5
kilometers = 9

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros.")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas.")

separador(4)
#comentari de l'alex

separador(5)


horas_trabajadas = float(input("Ingrese el número de horas trabajadas: "))
costo_por_hora = float(input("Ingrese el costo por hora: "))

paga = horas_trabajadas * costo_por_hora

print(f"La paga correspondiente es: {paga}")

separador(6)

n = int(input("Ingrese un número entero positivo: "))

if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    
    suma = n * (n + 1) // 2
    
    
    print(f"La suma de los enteros desde 1 hasta {n} es: {suma}")

separador(7)

peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

imc = peso / (estatura ** 2)

imc = round(imc, 2)

print(f"Tu índice de masa corporal es {imc}")

separador(8)

cantidad_invertir = float(input("Ingrese la cantidad a invertir: "))
interes_anual = float(input("Ingrese el interés anual (%): "))
num_anios = int(input("Ingrese el número de años: "))

interes_anual /= 100

capital_obtenido = cantidad_invertir * (1 + interes_anual) ** num_anios

print(f"El capital obtenido después de {num_anios} años es: {capital_obtenido}")

separador(9)

byte1 = input("Ingrese el primer byte de la dirección IP: ")
byte2 = input("Ingrese el segundo byte de la dirección IP: ")
byte3 = input("Ingrese el tercer byte de la dirección IP: ")
byte4 = input("Ingrese el cuarto byte de la dirección IP: ")


direccion_ip = f"{byte1}.{byte2}.{byte3}.{byte4}"
print(f"La dirección IP es: {direccion_ip}")

separador(10)

hora_inicio = int(input("Ingrese la hora de inicio: "))
min_inicio = int(input("Ingrese los minutos de inicio: "))
duracion = int(input("Ingrese la duración en minutos: "))
dia = int(input("Ingrese el día (1-30): "))


minutos_totales = hora_inicio * 60 + min_inicio + duracion
horas_totales = minutos_totales // 60
minutos_finales = minutos_totales % 60


dias_completos = horas_totales // 24
dia_final = dia + dias_completos
hora_final = horas_totales % 24


print(f"El evento finaliza el día {dia_final}, a las {hora_final:02d}:{minutos_finales:02d}")