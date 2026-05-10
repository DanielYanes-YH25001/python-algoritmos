def busqueda_secuencial(lista, objetivo):
  for i in range(len(lista)):
    if lista[i] == objetivo:
      return i  # Retorna el índice si lo encuentra
        
  # En caso el elemento no sea encontrado
  return -1

# Primer ejemplo de uso
numeros = [10, 32, 45, 96, 80, 77]
numero_objetivo = 80
resultado_1 = busqueda_secuencial(numeros, numero_objetivo)

if resultado_1 != -1:
    print(f"Elemento encontrado en el índice: {resultado_1}") # Resultado: 4
else:
    print("Elemento no encontrado")

# Segundo ejemplo de uso
empleados = [
   {"id": "1", "nombre_completo": "Juan Pérez", "edad": 24},
   {"id": "3", "nombre_completo": "Daniel Yanes", "edad": 20},
   {"id": "7", "nombre_completo": "Fabricio Torres", "edad": 21}
]

empleado_objetivo = {"id": "3", "nombre_completo": "Daniel Yanes", "edad": 20}
resultado_2 = busqueda_secuencial(empleados, empleado_objetivo)

if resultado_2 != -1:
    print(f"Elemento encontrado en el índice: {resultado_2}") # Resultado: 1
else:
    print("Elemento no encontrado")
    