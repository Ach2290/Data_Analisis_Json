import pandas as pd
from datetime import datetime
import json

# Cargar datos desde el archivo JSON
with open('employees.json', 'r') as file:
    respuesta = json.load(file)

# filtrar empleados menores de 30 años y que no pertenezcan al proyecto 'GRONK'
filtrados = [emp for emp in respuesta if emp["proyect"] != "GRONK"]

# modificar datos filtrados
for empleado in filtrados:
    empleado["salary"] = f'{float(empleado["salary"].replace("$", "").replace(",", "")) * 1.1:.2f}€'

df = pd.DataFrame(filtrados)
fecha = datetime.now().strftime("%m-%Y")

nombre_archivo = f"pagos-empleados-{fecha}.xlsx"
df.index.name= 'ID'
df.to_excel(nombre_archivo)

print(f"Archivo Excel '{nombre_archivo}' creado con éxito.")