#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)


separador(1)

print("1", "2", "3", "4", "5", sep=",", end=",")

separador(2)

print('"Estoy"')
print("'Algunos símbolos'")
print("''Son difíciles de imprimir: '/'\" ''")
print("I'm a programmer!!")

separador(3)

print("I'm Monty Python.")

separador(4)

resultat = ((3+2)/(2*5)) ** 2
print(resultat)