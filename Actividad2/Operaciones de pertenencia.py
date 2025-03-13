#operadores de pertenencia
lista = [1, 2, 3, 4, 5]
print(1 in lista)
print(6 in lista)#imprime False
print(1 not in lista)#imprime False
print(6 not in lista)
aprobado = float(input("Ingresa tu calificación: ")) >= 70
print("¿Aprobaste?:", aprobado)