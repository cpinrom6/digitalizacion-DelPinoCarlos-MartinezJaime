frase = input ("Escriba usted una frase: ")
p_prohibida = input ("Escriba usted la palabra prohibida: ")
contador = ""

if p_prohibida in frase: 
    for letra in p_prohibida:
        contador += "*"
    
    frase = frase.replace(p_prohibida, contador)
    print (frase)

else:
    print (f"La palabra prohibida no esta en la frase, por lo cual: {frase}")
