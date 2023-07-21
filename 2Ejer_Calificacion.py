print("     Calificaciones")

try:
    puntos=float(input("Por favor, introduzca su puntuación entre 0.0 y 1.0: "))
    if puntos > 1.0:
        print("\nPuntuación incorrecta")
    elif puntos >= 0.9:
        print("\nSobresaliente")
    elif puntos >= 0.8:
        print("\nNotable")
    elif puntos >= 0.7:
        print("\nBien")
    elif puntos >= 0.6:
        print("\nSuficiente")
    else:
        print("\nInsuficiente")
except:
    print("\nPuntuación incorrecta")