from dataclasses import dataclass
from distutils.log import info
from tkinter import filedialog, ttk
from tkinter import *

from PIL import Image, ImageTk
import csv
import os
import sys

#integrantes
#Eduardo M.
#Benjamin M.


#  ... Base de la Interfaz Gráfica ...   #
root = Tk()
root.title("CSV"); root.config(bg="#454545")
root.geometry("1240x1000")
root.resizable(True, True)


#----------------------------------------#
# ... Clases a utilizar en Vehículos ... #
#----------------------------------------#

@dataclass
class Vehiculo:
    tipoV: str
    costo: int
    def cantidad(self, capacity, name, tl):
        c = 0; c2 = 0
        for x in range(0, tl, capacity):
            c += 1
            
        
        print(f"Son {c} {name} en total")
        return c

@dataclass
class Barco(Vehiculo):
    capacidad: int

@dataclass
class Tren(Vehiculo):
    capacidad: int

@dataclass
class Avion(Vehiculo):
    capacidad: int

@dataclass
class Camion(Vehiculo):
    capacidad: int



#-------------------------------------------#
# ... Clases a utilizar en Contenedores ... #
#-------------------------------------------#

@dataclass
class Transporte:
    tipo_carga: str
    masa: str
    tonelaje: int
    tamanho: str = ""

    def cContenedores(self, tl):
        op = tl // self.tonelaje
        print(f"se requieren {op} contenedores {self.tipo_carga} de tamaño {self.tamanho}")
        return op


@dataclass
class ContenedorN(Transporte):

    def __post_init__(self):
        if self.tonelaje <= 12000:
            self.tamanho = "pequeño"
        else:
            self.tamanho = "grande"

        
@dataclass
class ContenedorR(Transporte):

    def __post_init__(self):
        if self.tonelaje <= 10000:
            self.tamanho = "pequeño"
        else:
            self.tamanho = "grande"


 
@dataclass
class Estanque(Transporte):

    def __post_init__(self):
        if self.tonelaje <= 10000:
            self.tamanho = "pequeño"
        else:
            self.tamanho = "grande"
        


#-----------------#
# ... Objetos ... #
#-----------------#

#----- Vehículos -----#
barco = Barco('Barco', 1000000000, 24000)
tren = Tren('Tren', 10000000, 250)
avion = Avion('Avion', 1000000, 10)
camion = Camion('Camion', 500000, 1)


#----- Contenedores -----#
ns = ContenedorN("normal", "solida", 24000)
nl = Estanque("normal", "liquida", 24000)
ng = Estanque("normal", "gas", 24000)

rs = ContenedorR("refrigerada", "solida", 20000)
rl = Estanque("refrigerada", "liquida", 20000)
rg = Estanque("refrigerada", "gas", 20000)

Is = ContenedorN("inflamable", "solida", 22000)
Il = Estanque("inflamable", "liquida", 22000)
Ig = Estanque("inflamable", "gas", 22000)   


#------------------#
# ... Funciones ... #
#------------------#

def mult(num, n):
    return [num * i for i in range(1, n + 1)]


def filtDates():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    all = []; total = 0
    c1 = 0; c2 = 0; c3 = 0
    c4 = 0; c5 = 0; c6 = 0
    c7 = 0; c8 = 0; c9 = 0
    archivo = filedialog.askopenfilename(title="Abrir")
    sep = archivo.split("/")

    with open(str(sep[-1])) as elements:
        reader = csv.reader(elements)
        for product in reader:
            try:
              all.append(product)
              total += int(product[4])
            except Exception as e:
                print(f"{product[4]} es un String\n")

        for x in range(len(all)):
            for y in range(len(all[x])):
                if all[x][2] == "normal" and all[x][3] == "solida":
                    if all[x][y] == all[x][4]:
                        c1 += int(all[x][4])

                elif all[x][2] == "normal" and all[x][3] == "liquida":
                    if all[x][y] == all[x][4]:
                        c2+= int(all[x][4])

                elif all[x][2] == "normal" and all[x][3] == "gas":
                    if all[x][y] == all[x][4]:
                        c3+= int(all[x][4])
                
                elif all[x][2] == "refrigerado" and all[x][3] == "solida":
                    if all[x][y] == all[x][4]:
                        c4+= int(all[x][4])

                elif all[x][2] == "refrigerado" and all[x][3] == "liquida":
                    if all[x][y] == all[x][4]:
                        c5+= int(all[x][4])

                elif all[x][2] == "refrigerado" and all[x][3] == "gas":
                    if all[x][y] == all[x][4]:
                        c6+= int(all[x][4])

                elif all[x][2] == "inflamable" and all[x][3] == "solida":
                    if all[x][y] == all[x][4]:
                        c7+= int(all[x][4])

                elif all[x][2] == "inflamable" and all[x][3] == "liquida":
                    if all[x][y] == all[x][4]:
                        c8+= int(all[x][4])
                
                elif all[x][2] == "inflamable" and all[x][3] == "gas":
                    if all[x][y] == all[x][4]:
                        c9+= int(all[x][4])
        
        print("Peso de normal solido:",c3)
        cn1 = ns.cContenedores(c1)
        cn2 = nl.cContenedores(c2)
        cn3 = ng.cContenedores(c3)

        cr1 = rs.cContenedores(c4)
        cr2 = rl.cContenedores(c5)
        cr3 = rg.cContenedores(c6)

        ei1 = Is.cContenedores(c7)
        ei2 = Il.cContenedores(c8)
        ei3 = Ig.cContenedores(c9)

        tl = cn1 + cn2 + cn3 + cr1 + cr2 + cr3 + ei1 + ei2 + ei3
        print("aqui",tl)
        v1 = barco.cantidad(barco.capacidad, barco.tipoV, tl)
        v2 = tren.cantidad(tren.capacidad, tren.tipoV, tl)
        v3 = avion.cantidad(avion.capacidad, avion.tipoV, tl)
        v4 = camion.cantidad(camion.capacidad, camion.tipoV, tl)
        
        print("total",tl)

        return


#-----------------------------#
# ... Funciones de Tkinter... #
#-----------------------------#
def loadIMG(IMG):
    image = Image.open(IMG)
    image = image.resize((300, 250), Image.ANTIALIAS)
    return image


    

#-----------------------------#
#    ... Interfaz ...         #
#-----------------------------#


#etiquetas de informacion de cada vehiculo


#aqui debe ir la informacion(prueba*)
infoBarco= "\nLa Lista de contenedores es:...\nCantidad total de cada tipo de Contenedor es:....\nTonelaje Total de Productos:....\nTonelaje por tipo de Producto:\nTonelaje por Masa"
infoTren= "aqui va la informacion del tren7272"
infoAvion= "aqui va la informacion del avion729d"
infoCamion= "aqui va la informacion del camion jddjjdd"

#funciones de info de transporte 
def botonInfoB():
    texto = Label(root, text=infoBarco,width=30,height=20,bg="pale turquoise").grid(row= 4,column=1)
def botonInfoT():
    texto = Label(root, text=infoAvion,width=30,height=20,bg="pale turquoise").grid(row= 4,column=2)
def botonInfoA():
    texto = Label(root, text=infoAvion,width=30,height=20,bg="pale turquoise").grid(row= 4,column=3)
def botonInfoC():
    texto = Label(root, text=infoCamion,width=30,height=20,bg="pale turquoise").grid(row= 4,column=4)




# Botones
b = loadIMG("barco.png")
ba = ImageTk.PhotoImage(b)
v1 = Button(root, image=ba, command=botonInfoB).grid(row=2,column=1)


t = loadIMG("tren.jpg")
tr = ImageTk.PhotoImage(t)
v2 = Button(root, image = tr,command=botonInfoT).grid(row=2,column=2)
a = loadIMG("avion.jpg")
av = ImageTk.PhotoImage(a)
v3 = Button(root, image = av,command=botonInfoA).grid(row=2, column=3)

c = loadIMG("camion.jpg")
ca = ImageTk.PhotoImage(c)
v4 = Button(root, image = ca,command=botonInfoC).grid(row=2, column=4)

#boton abre csv
op = Button(root, text="Abrir Carpeta", bg="green", width=20, height=5,borderwidth=5, relief="groove", command=filtDates).grid(row=0, column=1)


#label de informacion
labelti= Label(root, text="Optimizador de Contenedores\n1):Seleccione un archivo\n2):Luego toque una Imagen para ver mas Informacion",bg="pale green", width=50, height=5,font=('Helvetica', 14, 'bold')).place(x=250,y=0)



#prueba
x="aqui va el total"
labelCantidatT = Label(root, text=f"Cantidad total de Vehiculos es:{x}", bg="tomato2", width=40, height=5, borderwidth=5, relief="groove").grid(row=0,column=4)

#label de totales de vehiculo
labelCBarco = Label(root, text="La cantidad Total de Barcos Es:", bg="aquamarine",width=30, height=4, font=("Arial",10,'bold')).grid(row=1,column=1)
labelCTren = Label(root, text="La cantidad Total de Trenes Es:", bg="aquamarine",width=30, height=4, font=("Arial",10,'bold')).grid(row=1,column=2)
labelCAvion = Label(root, text="La cantidad Total de Aviones Es:", bg="aquamarine",width=30, height=4, font=("Arial",10,'bold')).grid(row=1,column=3)
labelCCamion = Label(root, text="La cantidad Total de Camiones Es:", bg="aquamarine",width=30, height=4, font=("Arial",10,'bold')).grid(row=1,column=4)


#label de informacion..
labelinfoB = Label(root, text="Informacion del Barco:", bg="cyan", width=30, height=3, font=("Arial",12,'bold')).grid(row=3,column=1)
labelinfoT = Label(root, text="Informacion del Tren:", bg="mediumpurple", width=30, height=3, font=("Arial",12,'bold')).grid(row=3,column=2)
labelinfoA = Label(root, text="Informacion del Avion:", bg="pink", width=30, height=3, font=("Arial",12,'bold')).grid(row=3,column=3)
labelinfoC = Label(root, text="Informacion del Camion:", bg="orange", width=30, height=3, font=("Arial",12,'bold')).grid(row=3,column=4)


#label costo
labelCostoTotal = Label(root, text="Costo Total:", bg="gold2", width=30, height=3, font=("Arial",12,'bold')).grid(row=6,column=1)
labelTotalesP= Label(root, text="Total Costos Parciales:", bg="gold1", width=30, height=3, font=("Arial",12,'bold')).grid(row=6,column=2)


root.mainloop()