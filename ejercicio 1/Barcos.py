objetivos = [
    ["-", "B", "-", "-", "-"],
    ["-", "-", "-", "-", "B"],
    ["-", "-", "-", "-", "-"],
    ["B", "-", "-", "-", "-"],
    ["-", "B", "-", "-", "-"]
]
barcos = [
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-"]
]
contador = 0
fila = None
columna = None
for linea in barcos:
    print(" ".join(linea))
    
print("") 
print("¿Donde quieres atacar?")

while contador < 4:
    fila = int(input("introduce la fila a la que quieres atacar: "))
    columna = int(input("introduce la columna a la que quieres atacar: "))
    
    if objetivos[fila-1][columna-1] == "B":
        print("¡Tocado y hundido!")
        barcos[fila-1][columna-1] = "X"
        objetivos[fila-1][columna-1] = "X"
        contador += 1
        for linea in barcos:
            print(" ".join(linea))
    elif barcos[fila-1][columna-1] == "X" or barcos[fila-1][columna-1] == "O":
        print("Ya has atacado esta posición. ¡Intenta otra!")
    else:
        print("Agua")
        barcos[fila][columna] = "O"
        
        
print("you WIN")