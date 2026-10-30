usuario=0
pin =0
intentos=0
terminado = False

print("introduzca pin y usuario")

while not terminado:
    usuario = input("introduzca el usuario: ")
    pin = input("introduzca la contraseña: ")
    
    if usuario != "root" or pin != "1234":
        print("datos incorrectos")
        intentos +=1
        print(f"has gastado {intentos} de los 3 intentos")
        if intentos == 3:
            print("has agotado tus intentos, sistema bloqueandose")
            terminado = True
    else:
        print("datos correctos, accediendo al sistema")
        terminado = True