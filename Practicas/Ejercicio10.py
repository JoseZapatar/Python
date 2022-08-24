"""Dado el numero de cuenta, el saldo y el monto de retiro de una cuenta de ahorra verifique
si la persona puede realizar el retiro. Una vez evaluado debe mostrarse el saldo que queda
después del retiro.
"""
numC = int(input("Digite su numero de cuenta: "))
saldo = 1000
retiro = int(input("Digite la cantidad que desea retirar: "))
if retiro>saldo:
    print("No tiene esa cantidad de dinero")
else:
    saldo -= retiro
    print(f"Numero de cuenta: {numC}")
    print(f"Su saldo actual es de:  {saldo}")