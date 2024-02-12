
import json

# Cargar datos desde el archivo JSON
with open('employees.json', 'r') as file:
    respuesta = json.load(file)

# Filtrar empleados menores de 30 años y que no pertenezcan al proyecto 'GRONK'
empleados_filtrados = [empleado for empleado in respuesta if empleado["age"] < 30 and empleado["proyect"] != "GRONK"]


