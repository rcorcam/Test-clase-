#Introducir la medida de números enteros de un triángulo y ver si es equilatero o no 

lado1 = int(input("Introduce el primer lado: "))
lado2 = int(input("Introduce el segundo lado: "))
lado3 = int(input("Introduce el tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
else:
    print("El triángulo NO es equilátero")