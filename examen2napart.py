#/usr/bin/env python3

def separador(exercici):
    print("")
    print("#" * 25)
    print("#")
    print("# Exercici " + str(exercici))
    print("#")
    print("#" * 25)



separador(1)

def calcula_pes_import(preu_kilo, pes):
    return pes * preu_kilo

print(f"Mig kilo de taronges = {calcula_pes_import(0.5, 1.70)}€")

separador(2)

articles = ["poma", "pera", "taronges"]
preus = [2.00, 3.00, 1.70]



while True:
    print("1 -", articles[0], preus[0],"€")
    print("2 -", articles[1], preus[1],"€")
    print("3 -", articles[2], preus[2],"€")
    print("0 - sortir")
    prem_tecla = input("Prem una tecla: ")
    if prem_tecla == "0":
        print("Adéu!Torna aviat a comprar")
        break
    elif prem_tecla == "1":
        kilos = float(input("Quants quilos vols? "))
        print(f"El preu és de: {calcula_pes_import(kilos, preus[0])}€")
        print(f"**************************************")
        print(f"{articles[0]} {preus[0]} x {kilos} = {calcula_pes_import(kilos, preus[0])}€")
        print(f"**************************************")      
    elif prem_tecla == "2":
        kilos = float(input("Quants quilos vols? "))
        print(f"El preu és de: {calcula_pes_import(kilos, preus[1])}€")
        print(f"**************************************")
        print(f"{articles[1]} {preus[1]} x {kilos} = {calcula_pes_import(kilos, preus[1])}€")
        print(f"**************************************")
    elif prem_tecla == "3":
        kilos = float(input("Quants quilos vols? "))
        print(f"El preu és de: {calcula_pes_import(kilos, preus[2])}€")
        print(f"**************************************")
        print(f"{articles[2]} {preus[2]} x {kilos} = {calcula_pes_import(kilos, preus[2])}€")
        print(f"**************************************")
    else:
        print("Valor no vàlid")

separador(4)

with open ("ticket.txt","a") as file:
    file.write("**************************************")
     #file.write(f"{articles[prem_tecla-1]} {preus[prem_tecla-1]} x {kilos} = {calcula_pes_import(kilos, preus[-1])}€")
    file.write("**************************************")

