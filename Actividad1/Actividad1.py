# Solicitar datos al usuario
nombre_completo = input("Ingrese su nombre completo: ")  # Tipo str
semestre = int(input("Ingrese su semestre (número entero): "))  # Tipo int
grupo = input("Ingrese su grupo: ")  # Tipo str
carrera = input("Ingrese su carrera: ")  # Tipo str

# Mostrar los datos ingresados
print("\n--- Información del estudiante ---")
print(f"Nombre completo: {nombre_completo}")
print(f"Semestre: {semestre}")
print(f"Grupo: {grupo}")
print(f"Carrera: {carrera}")

# Ejemplo de operadores
print("\n--- Operaciones con los datos ---")
print(f"El próximo semestre será: {semestre + 1}")  # Operador aritmético +
print(f"¿El semestre ingresado es mayor que 1? {semestre > 1}")  # Operador relacional >
print(f"¿El usuario está en primer semestre y en el grupo 'A'? {semestre == 1 and grupo.upper() == 'A'}")  # Operador lógico and