#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)



separador(1)

def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")


separador(2)

def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    days_per_month = [31, 28 + is_year_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None
    return days_per_month[month - 1]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")

separador(3)

def is_year_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(year, month):
    days_per_month = [31, 28 + is_year_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month < 1 or month > 12:
        return None
    return days_per_month[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None
    days_in_previous_months = sum(days_in_month(year, m) for m in range(1, month))
    return days_in_previous_months + day

print(day_of_year(2000, 12, 31))
separador(4)

def quadrat(num):
    return num ** 2

def arrel(num):
    return num ** 0.5

def pitagoras(a, c):
    b_quadrat = quadrat(c) - quadrat(a)
    return arrel(b_quadrat)

print(pitagoras(3, 5))  

separador(4)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

separador(7)

import math

def circle_area(radius):
    return math.pi * radius ** 2

def cylinder_volume(radius, height):
    return circle_area(radius) * height


radius = 5
height = 10
print("Área del círculo:", circle_area(radius))
print("Volumen del cilindro:", cylinder_volume(radius, height))

separador(8)

def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)


separador(9)

def es_vocal(letra):
    vocales = "aeiouAEIOU"
    return letra in vocales

def treu_vocals(palabra):
    return "".join(letra for letra in palabra if not es_vocal(letra))

def treu_consonants(palabra):
    return "".join(letra for letra in palabra if es_vocal(letra))


palabra = "Hola Mundo"
print("Palabra sin vocales:", treu_vocals(palabra))
print("Solo vocales:", treu_consonants(palabra))