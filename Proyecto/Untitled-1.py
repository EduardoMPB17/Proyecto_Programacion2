from dataclasses import dataclass
import csv

@dataclass
class Producto:
    Id : int
    Nombre_producto : str
    Tipo : str
    Masa : str
    Peso : int


@dataclass#se ve de  mejor manera las clases y mas ordenadas
class ContenedorNormal_Pequeño:
    Id : int
    Nombre_producto : str
    Tipo : str
    Masa : str
    Peso : int
@dataclass
class ContenedorNormal_Grande:
    Id : int
    Nombre_producto : str
    Tipo : str
    Masa : str 
    Peso : int 
@dataclass
class ContenedorRefrigerado_Pequeño:
    Id : int
    Nombre_producto : str
    Tipo : str
    Masa : str
    Peso : int
@dataclass
class ContenedorRefrigerado_Grande:
    Id : int 
    Nombre_producto : str 
    Tipo : str 
    Masa : str 
    Peso : int 
@dataclass
class Estanque_liquidos:
    Id : int 
    Nombre_producto : str 
    Tipo : str 
    Masa : str 
    Peso : int 
@dataclass
class Estanque_liquidos_inflamables:
    Id : int 
    Nombre_producto : str 
    Tipo : str 
    Masa : str 
    Peso : int 


#Abre el archivo lo lee y guarda en una lista 
with open('ejemplo_lista.csv', newline='') as csvfile:
    lista = []
    lector = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in lector:
        lista.append(row)
        print(lista)

print("::::::::::::::::::::::::::::::::::::::::::::::::")
for rw in lista:
    for elemento in rw:
        print(elemento)#para verlo mejor
        

for i in lista[3]:
    print(i)

