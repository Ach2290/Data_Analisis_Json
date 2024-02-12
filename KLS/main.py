import pandas as pd
from datetime import datetime
import json

# Cargar datos desde el archivo JSON
with open('employees.json', 'r') as file:
    respuesta = json.load(file)

# filtrar empleados menores de 30 años y que no pertenezcan al proyecto 'GRONK'
filtrados = [e for e in respuesta if e("proyect") != "GRONK"]

# modificar datos filtrados
for empleado in filtrados:
    empleado["salary"] = f'{float(empleado["salary"].replace("$", "").replace(",", "")) * 1.1:.2f}€'

df = pd.DataFrame(filtrados)
mes_y_anio = datetime.now().strftime("%m-%Y")