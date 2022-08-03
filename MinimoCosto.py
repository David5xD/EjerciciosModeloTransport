import numpy as np
from scipy import optimize
import pulp
from pyomo.environ import *
from pyomo.opt import SolverFactory
import pyomo.environ

np.random.seed(1984) #replicar random

print('EJERCICIO #2 (Metodo de Min. Costo)')
# Ejemplo del problema de transporte de las granjas
# Creamos la variable prob que contiene los datos del problema
prob = pulp.LpProblem("Problema de distribución de cerveza", pulp.LpMinimize)

# Creamos lista de granjas o nodos de oferta
cervecerias = ["Granja A", "Granja B", "Granja C"]

# diccionario con la capacidad de oferta de cada granja
oferta = {"Granja A": 10,
          "Granja B": 20,
          "Granja C": 10}

# Creamos la lista de almacenes o nodos de demanda
bares = ["Almacén 1", "Almacén 2", "Almacén 3", "Almacén 4"]

# diccionario con la capacidad de demanda de cada almacen
demanda = {"Almacén 1":5,
           "Almacén 2":15,
           "Almacén 3":15,
           "Almacén 4":15}

# Lista con los costos de transporte de cada nodo
costos = [   #Almacen
         #1 2 3 4
         [10,2,20,11],#A   Granjas
         [12,7,9,20],#B
         [4,14,16,18] #C

         ]

# Convertimos los costos en un diccionario de PuLP
costos = pulp.makeDict([cervecerias, bares], costos,0)

# Creamos una lista de tuplas que contiene todas las posibles rutas de tranporte.
rutas = [(c,b) for c in cervecerias for b in bares]

# creamos diccionario x que contendrá la candidad enviada en las rutas
x = pulp.LpVariable.dicts("ruta", (cervecerias, bares),
                        lowBound = 0,
                        cat = pulp.LpInteger)

# Agregamos la función objetivo al problema
prob += sum([x[c][b]*costos[c][b] for (c,b) in rutas]), \
            "Suma_de_costos_de_transporte"

# Agregamos la restricción de máxima oferta de cada granja al problema.
for c in cervecerias:
    prob += sum([x[c][b] for b in bares]) <= oferta[c], \
            "Suma_de_Productos_que_salen_de_granjas_%s"%c

# Agregamos la restricción de demanda mínima de cada almacen
for b in bares:
    prob += sum([x[c][b] for c in cervecerias]) >= demanda[b], \
    "Sum_of_Products_into_Almacen%s"%b

# Los datos del problema son exportado a archivo .lp
prob.writeLP("problemaDeTransporte.lp")

# Resolviendo el problema.
prob.solve()

# Imprimimos el estado del problema.
print("Status: {}".format(pulp.LpStatus[prob.status]))

# Imprimimos cada variable con su solución óptima.
for v in prob.variables():
    print("{0:} = {1:}".format(v.name, v.varValue))

# Imprimimos el valor óptimo de la función objetivo
print("Costo total de transporte = {}".format(prob.objective.value()))