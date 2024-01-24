#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)



separador(1)

numero_natural = int(input("Di un numero natural: "))
pasos = 0
c0 = numero_natural

while c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3* c0 + 1
    pasos += 1

print(f"se alcanza 1 en {pasos} pasos")

separador(2)

beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(beatles)

for i in range(2):
    new_beatle = input("digues un membre: ")
    beatles.append(new_beatle)

print(beatles)

del beatles[-2:]

    
beatles.insert(0, "Ringo Starr")

print(beatles)

separador(3)

def ord_burbuja(arreglo):
    n = len(arreglo)

    for i in range(n-1):
        for j in range(n-1-i):
            if arreglo[j] > arreglo[j+1]:
                arreglo[j], arreglo[j+1] = arreglo[j+1], arreglo[j]

lista = [8, 3, 1, 19, 14]
ord_burbuja(lista)

print(lista)

separador(4)

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

my_list_unicos = []

for i in my_list:
    if i not in my_list_unicos:
        my_list_unicos.append(i)



print("La lista con elementos únicos: ")
print(my_list_unicos)

separador(5)

lista = []
numeros_ganadores = lista

for i in range(3):
    numeros_ganadores = int(input('cuales son los numeros gandores? '))
    lista.append(numeros_ganadores)


print(lista)

lista.sort()

print(lista)

separador(6)

lista_suspendida = []

lista_assignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for i in lista_assignaturas:
    print(i)
    nota = int(input("Que nota has sacado en cada assignatura? "))
    if nota < 5:
        lista_suspendida.append(i)
print(lista_suspendida)



separador(7)

usuario_palabra = input("Ingresa una palabra: ")

palabra = usuario_palabra.lower().replace(" ", "")

if palabra == palabra[::-1]:
    print("ES palíndromo")
else:
    print("NO es palíndromo")

