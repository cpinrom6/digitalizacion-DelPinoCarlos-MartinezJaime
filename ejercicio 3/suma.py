suma = 0
contador = 1

n1 = float(input("dime un numero: "))
suma +=n1
while contador < 10 and suma <= 100:
    contador +=1
    suma+=n1
    n1 = float(input("dime otro numero: "))

if contador == 10 and suma < 100:
    print("el proceso se ha terminado debido a que se han introducido 10 numeros")
elif suma > 100 and contador < 10:
    print("el proceso se ha terminado debido a que se ha introducido una suma mayor que 100")
elif suma > 100 and contador == 10:
    print("el proceso se ha terminado debido a que se ha introducido una suma mayor que 100”)