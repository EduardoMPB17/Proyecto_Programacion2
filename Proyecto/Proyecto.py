from ctypes import wstring_at
from dataclasses import dataclass
import csv

with open('indicator.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))



# @dataclass
# class vehiculo:
#     barco:str
#     tren:str
#     avion:str
#     camion:str
    
#     if __name__ == '__main__':
        

# class Contendor:
#     normal_pequeño:str
#     normal_grande:str
#     refrigarado_pequeño:str
#     refrigarado_grande:str
#     estanque_liquidos:str
#     estanque_liquidos_inflamables:str
#     if __name__ == '__main__':