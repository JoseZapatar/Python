"""Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
estudiante de manera individual, escriba un código en Python que permita crear un correo
electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
“@est.uca.edu.ni
”"""
correo = []
nombre1 = input("Escriba su primer nombre: ")
correo.append(nombre1)
nombre2 = input("Escriba su segundo nombre: ")
correo.append(nombre2)
apellido1 = input("Escriba su primer apellido: ")
correo.append(apellido1)
apellido2 = input("Escriba su segundo apellido: ")
correo.append(apellido2)
print(f"Su correo electronico es: {correo[0]}.{correo[2]}@est.uca.edu.ni")
