# Mostrar si un triángulo es equilátero, isósceles o escaleno

l1 = int(input("Dame el valor de l1: "))
l2 = int(input("Dame el valor de l2: "))
l3 = int(input("Dame el valor de l3: "))

if l1 == l2 == l3:
    print("El triángulo es equilátero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")+
    