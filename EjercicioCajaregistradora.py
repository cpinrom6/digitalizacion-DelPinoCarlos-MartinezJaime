dinero_cobrado = 1
total = 0
contador = 0

print ("Introduzca un 0 para indicar que la caja ya se ha cerrado")

while dinero_cobrado != 0:
    contador += 1
    dinero_cobrado = float(input (f"Cantidad cobrada de la cuenta {contador}: "))
    total += dinero_cobrado

print (f"Se ha cobrado un total de {total} €")

