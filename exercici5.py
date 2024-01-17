#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)



separador(1)

'''
import time

for i in range(1,6):
    print("mississippi")
    time.sleep(1)

def mensaje_final():
    print("¡Listos o no, ahí voy!")

mensaje_final()


separador(2)

while True:
    pregunta = input("di una palabra: ")
    if pregunta != "chupacabra":
        print("repite la palabra")
    else:
        print("¡Has dejado el bucle con éxito!")
        break

separador(3)

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

for letra in user_word:
    if letra in ["A", "E", "I", "O", "U"]:
        continue
    else:
        (letra)

separador(4)

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()

word_without_vowels = ""

for letra in user_word:
    if letra in ["A", "E", "I", "O", "U"]:
        continue
    else:
        word_without_vowels += letra
print("Palabra sin vocales:", word_without_vowels)



separador(5)
cantidad_a_invertir = int(input("Cual es tu cantidad a invertir? "))
interes = int(input("interes anual:" ))
numero_años  = int(input("numero de años: "))
cantidad_final = cantidad_a_invertir
for i in range(numero_años):
    dinero_ganado = cantidad_a_invertir * (interes / 100)

    cantidad_final += dinero_ganado

    print(f"Capital obtenido = {dinero_ganado:}, Total acumulado = {cantidad_final:}")

separador(6)

altura = int(input("dime un numero entero para la altura del triángulo: "))

for i in range(1, altura + 1):
    print('*' * i)




altura = int(input("dime un numero entero para la altura del triángulo: "))

for i in range(1, altura + 1):
    for j in range(i, 0, -1):
        print(j, end='')
    print()

separador(7)

numero_entero = int(input("Dime un numero entero: "))

primo = True
for divisor in range(2,numero_entero):
    if numero_entero % divisor == 0:
        print("no es primo")
        primo = False
        break
    
if primo == True:
    print("És primo com el meu cosí :D")
        

separador(8)

palabra = input("Introduce una palabra: ")

for letra in reversed(palabra):
    print(letra)

separador(9)

frase = input("Dime una frase: ")
letra = input("Dime una letra: ")
contador = 0

for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"la letra {letra} aparece {contador} vezes en la frase")
'''
separador(10)

blocks = int(input("Ingresa el número de bloques: "))
altura = 0
bloques_utilizados = 0

while bloques_utilizados <= blocks:
    altura += 1
    bloques_utilizados += altura

if bloques_utilizados > blocks:
    altura -= 1

print("La altura de la pirámide es:", altura)

