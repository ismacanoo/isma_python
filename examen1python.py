#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)

separador(1)

print('Benvingut "client". L’ajudarem a calcular el pressupost.')
print('Quin vehicle té?')
print('C Cotxe')
print('M Moto')
print('X Exit')

vehicle = input('Introdueixi C per Cotxe, M per Moto o X per sortir: ')

if vehicle == "C":
    print("Preu Base 400€")
    preu_final = 400
    
if vehicle == "M":
    print("Preu Base 300€")
    preu_final = 300
if vehicle == "X":
    print("Adeu, gràcies!")

separador(2)

anys_carnet = int(input("Anys de carnet? "))

if anys_carnet < 10:    
    penalitzacio = 100
    preu_final += penalitzacio
    print(f"Penalització {penalitzacio}€ preu final {float(preu_final)}€")

if anys_carnet > 10:
    bonificació = 1-((anys_carnet - 10)* 0.01)
    preu_final -= bonificació
    print(f"Bonificació per experiència {bonificació}% preu final {float(preu_final)}€")

separador(3)

partes_contra = int(input("Quants partes en contra tens en el darrer any?" ))

if partes_contra == 0:
    bonificació *= 0.9
    preu_final -= bonificació
    print(f"Bonificació {bonificació}")
    print(f"Preu final {preu_final}")