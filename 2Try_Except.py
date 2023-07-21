print("     Calculo de salario\n")

try:
    horas = float(input("Introduzca las horas: "))
    tarifa = float(input("Introduzca la tarifa: "))
    total = horas*tarifa
    print(total)
except:
    print("Error, por favor introduzca un número")





