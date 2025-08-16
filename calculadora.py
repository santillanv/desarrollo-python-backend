print("|" + "*"*30 + "|\n")
print(" "*4,"1. Suma")
print(" "*4,"2. Resta")
print(" "*4,"3. Multiplicación")
print(" "*4,"4. División\n")
print("|" + "*"*30 + "|")
option = int(input("\nElije una opción:  "))

num1 = int(input("\nIngresa el primer número:  "))
num2 = int(input("\nIngresa el segundo número:  "))


if option == 1:
    print("La suma es: ",num1 + num2)
elif option == 2:
    print("La resta es: ",num1 - num2)
elif option == 3:
    print("La multiplicación es: ",num1 * num2)
elif option == 4:
    if num2 != 0:
        print("La división es: ",num1 / num2)
    else:
        print("No se puede dividir entre cero.")
else:
    print("Opción incorrecta.")
