#Leer dos números y decir cual es mayor y cual es menor.
num1 = int(input(f"Digite un numero: "))
num2 = int(input(f"Digite otro numero: "))

if num1>num2:
    print(f"El numero mayor es: {num1} \n  El numero menor es: {num2} ")
elif num2>num1:
    print(f"El numero mayor es: {num2}\n El numero menor es: {num1} ")
elif num1==num2:
    print("Los numeros son iguales")