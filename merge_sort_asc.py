def merge_sort(lista):
  if len(lista) > 1:
    medio = len(lista) // 2
    izquierda = lista[:medio]
    derecha = lista[medio:]

    # Ordenamos recursivamente la parte izquierda y derecha
    merge_sort(izquierda)
    merge_sort(derecha)

    i = j = k = 0

    # Mezclamos las sublistas ordenadas
    while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
        lista[k] = izquierda[i]
        i += 1
      else:
        lista[k] = derecha[j]
        j += 1
      k += 1

    # Verificamos los elementos restantes
    while i < len(izquierda):
      lista[k] = izquierda[i]
      i += 1
      k += 1

    while j < len(derecha):
      lista[k] = derecha[j]
      j += 1
      k += 1

  # Finalmente retornamos la lista final ordenada
  return lista

# Ejemplo de uso (forma ascendente)
lista_numerica = [38, 27, 43, 3, 9, 82, 10]
merge_sort(lista_numerica)
print(lista_numerica) # Resultado: [3, 9, 10, 27, 38, 43, 82]
