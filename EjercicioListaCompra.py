compra = ["pan", "leche ", "huevos"]

print ("La lista de la compra es actualmente: ", compra)

producto_añadido1 = input ("Añada un producto a la lista: ")
compra.append(producto_añadido1)

producto_añadido2 = input ("Añada un producto a la lista: ")
compra.insert(0,producto_añadido2)

print ("La lista de la compra es actualmente: ", compra)

producto_eliminado = input ("Elimine uno de los productos: ")
compra.remove(producto_eliminado)

ultimo = compra.pop()
print ("Se ha eliminado el ultimo poducrto de la lista, el cual era: ", ultimo)

print ("La lista de la compra es actualmente: ", compra)
print ("la lista tiotal de porductos", len(compra))
