#Introducir una letra y sies A realizaremos el área de una circunferencia y si es L realizar el área de una circunferencia 
import math

letra = input("Introduce una letra (A = Área / L = Longitud): ").upper()
radio = float(input("Introduce el radio de la circunferencia: "))

if letra == "A":
    area = math.pi * radio ** 2
    print(f"El área de la circunferencia es: {area:.2f}")
elif letra == "L":
    longitud = 2 * math.pi * radio
    print(f"La longitud de la circunferencia es: {longitud:.2f}")
else:
    print("Opción no válida. Debes introducir A o L.")