def busqueda_binaria(lista, objetivo):
  izquierda = 0
  derecha = len(lista) - 1

  while izquierda <= derecha:
    idx_numero_central = (izquierda + derecha) // 2 # Índice del número central
    numero_central = lista[idx_numero_central] # Número central

    if numero_central == objetivo:
      return idx_numero_central # En caso el número central corresponda al número objetivo
    elif numero_central < objetivo:
      izquierda = idx_numero_central + 1 # Descartamos todos los números de la izquierda
    else:
      derecha = idx_numero_central - 1 # Descartamos todos los números de la derecha

  # En caso el elemento no sea encontrado
  return -1

# Ejemplo de uso
lista_numerica = [1, 3, 5, 7, 9, 11, 13]
print(busqueda_binaria(lista_numerica, 7))  # Resultado: 3
