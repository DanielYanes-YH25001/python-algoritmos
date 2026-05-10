def quicksort(lista):
  # Caso base, cuando la lista no tenga números o solo tenga un número
  if len(lista) <= 1:
    return lista
  else:
    # Seleccionamos el pivote (en este caso, el último número)
    pivote = lista.pop()
        
    items_mayores = []
    items_menores = []
    
    # Particionamos
    for item in lista:
      if item > pivote:
        items_mayores.append(item)
      else:
        items_menores.append(item)
            
    # Ordenamos y combinamos de manera recursiva
    return quicksort(items_mayores) + [pivote] + quicksort(items_menores)

# Ejemplo de uso (forma descendente)
lista_numerica = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(lista_numerica)) # Resultado: [10, 8, 6, 3, 2, 1, 1]
