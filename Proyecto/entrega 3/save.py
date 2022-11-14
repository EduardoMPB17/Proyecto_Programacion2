from dataclasses import dataclass
from distutils.log import info
from tkinter import filedialog, ttk,messagebox
from tkinter import *
from fpdf import FPDF
from PIL import Image, ImageTk
import csv
import pyautogui
from matplotlib.pyplot import grid
import mysql.connector

#  ... Base de la Interfaz Gráfica ...   #
root = Tk()
root.title("CSV"); root.config(bg="#454545")
root.attributes("-fullscreen",True)
root.resizable(True, True)


# ----> Nombres: Benjamín Millanao, Eduardo Mariqueo. <---- 


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
            self.tamanho = "normal"
        else:
            self.tamanho = "inflamable"
        


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


#--------------------------#
# ... Código Principal ... #
#--------------------------#

# Con esta función lo que buscamos es recibir por tipo de contenedores
# los cuales son 3, en este caso usaríamos esta función para: Cont. Normales, Cont. Refrigerados y Estanques
def optimization2(cn):
    global cBar, cTr, cAv, cCa, calc, sumALL
    cBar = 0; cTr = 0; cAv = 0; cCa = 0; calc = 0
    capacidad = barco.capacidad
    sumALL = 0
    
    for q in range(0, cn, barco.capacidad):
        if barco.capacidad + q > cn:
            pass
        else:
            cBar += 1
    cn = cn - (cBar * barco.capacidad) 
    

    for w in range(0, cn, tren.capacidad):
        if tren.capacidad + w > cn:
            pass
        else:
            cTr += 1
    cn = cn - (cTr * tren.capacidad) 


    for e in range(0, cn, avion.capacidad):
        if avion.capacidad + e > cn:
            pass
        else:
            cAv += 1
    cn = cn - (cAv * avion.capacidad) 
    

    for r in range(0, cn, camion.capacidad):
        if camion.capacidad + r > cn:
            pass
        else:
            cCa += 1
    #sumALL = cBar + cTr + cAv + cCa

    return cBar, cTr, cAv, cCa


# Con esta función realizamos ciertos calculos que se requieren en la entrega
# Tales como la cantidad de cada vehículo, el total general de vehículos y el costo
def totalSUM(a, b, c):
    global totalVeh, bs, ts, ar, cs, monto, toneBar, toneTr, toneAv, toneCs, barcoCosto, trenCosto, avionCosto, camionCosto
    totalVeh = 0
    bs = 0; ts = 0; ar = 0; cs = 0
    empty = []
    for x in a:
        empty.append(x)
    bs += empty[0]
    ts += empty[1]
    ar += empty[2]
    cs += empty[3]

    for x in b:
        empty.append(x)
    bs += empty[4]
    ts += empty[5]
    ar += empty[6]
    cs += empty[7]

    for x in c:
        empty.append(x)
    bs += empty[8]
    ts += empty[9]
    ar += empty[10]
    cs += empty[11]
    
    for x in empty:
        totalVeh += x

    toneBar = bs * barco.capacidad
    toneTr = ts * tren.capacidad
    toneAv = ar * avion.capacidad
    toneCs = cs * camion.capacidad
    monto = (bs * barco.costo) + (ts * tren.costo) + (ar * avion.costo) + (cs * camion.costo)
    barcoCosto = bs * barco.costo
    trenCosto = ts * tren.costo
    avionCosto = ar * avion.costo
    camionCosto = cs * camion.costo
    return

#-----Conexion SQL --------------------------------
conexion=mysql.connector.connect(host="db.inf.uct.cl",#base de datos
                                user="A2022_emariqueo",
                                passwd="A2022_emariqueo", 
                                database="A2022_emariqueo")

cursorInsert = conexion.cursor()
cursorSelect = conexion.cursor()
cursorDelete = conexion.cursor()



# Esta función básicamente permite abrir un archivo.
# En este caso lo separamos con split en un arreglo, para separar el archivo del directorio
# y escogemos el último elemento, el cual correspondería exactamente
# al nombre del archivo: "MOCK_DATA.csv", etc...
def openfile():
    try:
        archivo = filedialog.askopenfilename(title="Abrir")
        elimina = cursorDelete.execute("DELETE FROM personas")#asegura que no se repita informacion,al ejecutar denuevo el programa
        conexion.commit()
        sep = archivo.split("/")
        return str(sep[-1])
    except:
        print("Error, no se abrió ningún archivo")


# Lo usamos más abajo, esta función es la de arriba y solo devolverá el nombre del archivo
# Ya que si no lo filtrabamos, filedialog nos devolvería el directorio completo.
file = openfile()


all = []; total = 0
cBar = 0
c1 = 0; c2 = 0; c3 = 0
c4 = 0; c5 = 0; c6 = 0
c7 = 0; c8 = 0; c9 = 0

# Acá leemos el archivo y asignamos 9 contadores,
# para ir filtrando por tipo + masa, según lo que requiere la entrega, también hacemos una suma total
# y agregamos los elementos en una lista general, para futuros cálculos
with open(file) as elements:
    next(elements)#omite el encabezado
    reader = csv.reader(elements)
    for product in elements:
                productS = product.split(",")
                id = productS[0]#valores
                nombre = productS[1]
                tipo = productS[2]
                masa = productS[3]
                peso = productS[4]
                
                cursorInsert.execute(f"INSERT INTO personas(id,nombre,tipo,masa,peso) VALUES ('{id}','{nombre}','{tipo}','{masa}','{peso}')")
                conexion.commit()#confirma la consultas sql
                
    print("se insertaron los datos correctamente")
    cursorSelect.execute("SELECT * FROM personas")#ejecuta la consultas a BD
    
    #-----------------------------------------------------
    lista_bd=[];all=[]; total=0
    
    for row in cursorSelect:#
        print(row)
        lista_bd.append(row)
    print("="*45)#
    r_list = []
    for tupla in lista_bd:#pasa las tuplas a lista en otra lista
        t_list = list(tupla)
        r_list.append(t_list)
        #print(r_list)probar la matriz
    
    for product in r_list:        
        all.append(product)
        total += int(product[4])
        
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
                        

cn1 = ns.cContenedores(c1)
cn2 = nl.cContenedores(c2)
cn3 = ng.cContenedores(c3)

cr1 = rs.cContenedores(c4)
cr2 = rl.cContenedores(c5)
cr3 = rg.cContenedores(c6)

ei1 = Is.cContenedores(c7)
ei2 = Il.cContenedores(c8)
ei3 = Ig.cContenedores(c9)


n = cn1 + cn2 + cn3
r = cr1 + cr2 + cr3
e = ei1 + ei2 + ei3
tl = n + r + e

barco.cantidad(barco.capacidad, barco.tipoV, tl)
tren.cantidad(tren.capacidad, tren.tipoV, tl)
avion.cantidad(avion.capacidad, avion.tipoV, tl)
camion.cantidad(camion.capacidad, camion.tipoV, tl)

tnormal = optimization2(n)
trefrigerado = optimization2(r)
tliquido = optimization2(e)


totalSUM(tnormal, trefrigerado, tliquido)

#-----------------------------#
# ... Funciones de Tkinter... #
#-----------------------------#
# Con esta función redimensionamos la imagen para que quede bien dentro de la interfaz,
# ya que por defecto estás imagenes realmente son grandes y la interfaz quedaría desigual.
def loadIMG(IMG):
    image = Image.open(IMG)
    image = image.resize((300, 255))
    return image


#-----------------------------#
#    ... Interfaz ...         #
#-----------------------------#
# 

#---------------------------------#
# --- Funciones de la interfaz ---#  

# Funciones de info de transporte 
def botonInfoB():
    texto = Label(root, text=infoBarco,width=44,height=20,bg="pale turquoise").grid(row= 4,column=1)
def botonInfoT():
    texto = Label(root, text=infoTren,width=44,height=20,bg="pale turquoise").grid(row= 4,column=2)
def botonInfoA():
    texto = Label(root, text=infoAvion,width=44,height=20,bg="pale turquoise").grid(row= 4,column=3)
def botonInfoC():
    texto = Label(root, text=infoCamion,width=44,height=20,bg="pale turquoise").grid(row= 4,column=4)


#funcion del boton para exportar a PDF
def exportarPDF():
    #pdf
    screenshot = pyautogui.screenshot(region=(30, 110, 1450, 910))#dimensiones de la captura
    sc= screenshot.save("captura.png")#guarda captura
    screenshot.show
    pdf = FPDF(orientation='P', unit = 'mm', format='A4')
    pdf.add_page()
    #pag 1 barco
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(60)
    pdf.cell(80, 10, 'Informacion de Contenedores', 1, 1, 'C')
    pdf.image("captura.png",w=195,h=250)#pone captura con dimensiones acorde al pdf
    
    #salida a pdf
    pdf.output('Informacion.pdf', 'F')
    

#funcion del boton de cambiar costos
def CambiaCostos():
    ventana=Tk()#ventana emergente
    ventana.title ("Modificar Costos")
    ventana.geometry("400x400+1500+200")#dimensiones
    
    def cambia():
        x1 = int(caja1.get()) #obtiene los entry del tkinter    
        x2 = int(caja2.get())
        x3 = int(caja3.get())     
        x4 = int(caja4.get())     
        tren.costo = x1#se supone que cambia los costos
        barco.costo = x2
        avion.costo = x3
        camion.costo = x4
        #totalSUM(tnormal, trefrigerado, tliquido)
        messagebox.showinfo(message=f"El Costo del Tren ahora es:{tren.costo}\nEl Costo del Barco ahora es:{barco.costo}\nEl Costo del Avion ahora es:{avion.costo}\nEL Costo del Camion ahora es:{camion.costo}",title= "Costos Actualizados")
        ventana.destroy()#cierra la ventana
        
    etiqueta = Label(ventana,text="Ingresa Los Nuevos Costos $", font=("Arial"),bg="wheat1")
    etiqueta1 = Label(ventana, text="Tren",bg="darkolivegreen1")
    caja1 = Entry(ventana)
    
    etiqueta2 = Label(ventana, text="Barco",bg="darkolivegreen1")
    caja2 = Entry(ventana)
    
    etiqueta3 = Label(ventana, text="Avion",bg="darkolivegreen1")
    caja3 = Entry(ventana)
    
    etiqueta4 = Label(ventana, text="Camion",bg="darkolivegreen1")
    caja4 = Entry(ventana)
    
    boton1 = Button(ventana, text="Aplicar Cambios",command=cambia)
    
    #orden del los label
    etiqueta.pack(padx=5,pady=5)
    etiqueta1.pack(padx=5,pady=5)
    caja1.pack(padx=5,pady=5)
    etiqueta2.pack(padx=5,pady=5)
    caja2.pack(padx=5,pady=5)
    etiqueta3.pack(padx=5,pady=5)
    caja3.pack(padx=5,pady=5)
    etiqueta4.pack(padx=5,pady=5)
    caja4.pack(padx=5,pady=5)
    boton1.pack(padx=5,pady=5)
    ventana.mainloop()

#---------------------------------#
# --- Botones ---#  

# Botones de Imganes de los vehiculos
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

# Botón abre csv
op = Button(root, text="Abrir otro Archivo", bg="green", width=20, height=4,borderwidth=5, relief="groove", command=openfile).grid(row=0, column=1)

#Boton cierra en pantalla completo
close = Button(root, text="X", bg="red",width=4,height=2,command=root.destroy).place(x=1880,y=0)

#boton cambia costo abre nueva ventana
cambiaC_T = Button(root, text="Modificar costos", bg="yellow2", width=15, height=2,borderwidth=10,command=CambiaCostos).grid(row=1, column=5)

#boton exportarpdf
pdf = Button(root, text="Exportar a PDF", bg="red", width=15, height=2 , borderwidth=10,command=exportarPDF).grid(row=0,column=4)

#---------------------------------#
# --- Etiquetas ---#  

#Variables de información de cada vehÍculo , Aquí va la información de cada vehículo(se muestran al presionar una imagen)
infoBarco= f"\nLa Lista de contenedores es:\nCantidad total de cada tipo de Contenedor es:....\nTonelaje Total de Productos: {toneBar} ton.\nTonelaje por tipo de Producto:\nTonelaje por Masa"
infoTren= f"\nLa Lista de contenedores es:\nCantidad total de cada tipo de Contenedor es:....\nTonelaje Total de Productos: {toneTr} ton.\nTonelaje por tipo de Producto:\nTonelaje por Masa"
infoAvion= f"\nLa Lista de contenedores es:\nCantidad total de cada tipo de Contenedor es:....\nTonelaje Total de Productos: {toneAv} ton.\nTonelaje por tipo de Producto:\nTonelaje por Masa"
infoCamion= f"\nLa Lista de contenedores es:\nCantidad total de cada tipo de Contenedor es:....\nTonelaje Total de Productos: {toneCs} ton.\nTonelaje por tipo de Producto:\nTonelaje por Masa"

# Label de informacion
labelti= Label(root, text="Optimizador de Contenedores\n1):Seleccione un archivo\n2):Toque una Imagen para ver mas Información",bg="pale green", width=40, height=3,font=('Helvetica', 14, 'bold')).place(x=280,y=0)

# labelCostos
labelCostos = Label(root, text="Toque el Boton de abajo\n para modificar los costos", bg="aqua", width=30, height=5 ).grid(row=0,column=5) 

#x = total(tnormal, trefrigerado, tliquido)
#label de vehiculos totales
labelCantidatT = Label(root, text=f"Cantidad total de Vehículos es: {totalVeh}", bg="skyblue1", width=30, height=5, relief="flat").grid(row=6,column=3)

# Label de totales de vehículo
labelCBarco = Label(root, text=f"La cantidad Total de Barcos Es: {bs}", bg="aquamarine",width=30, height=2, font=("Arial",10,'bold')).grid(row=1,column=1)
labelCTren = Label(root, text=f"La cantidad Total de Trenes Es: {ts}", bg="aquamarine",width=30, height=2, font=("Arial",10,'bold')).grid(row=1,column=2)
labelCAvion = Label(root, text=f"La cantidad Total de Aviones Es: {ar}", bg="aquamarine",width=30, height=2, font=("Arial",10,'bold')).grid(row=1,column=3)
labelCCamion = Label(root, text=f"La cantidad Total de Camiones Es: {cs}", bg="aquamarine",width=30, height=2, font=("Arial",10,'bold')).grid(row=1,column=4)


# Label de información..
labelinfoB = Label(root, text="Información del Barco:", bg="cyan", width=30, height=2, font=("Arial",12,'bold')).grid(row=3,column=1)
labelinfoT = Label(root, text="Información del Tren:", bg="mediumpurple", width=30, height=2, font=("Arial",12,'bold')).grid(row=3,column=2)
labelinfoA = Label(root, text="Información del Avión:", bg="pink", width=30, height=2, font=("Arial",12,'bold')).grid(row=3,column=3)
labelinfoC = Label(root, text="Información del Camión:", bg="orange", width=30, height=2, font=("Arial",12,'bold')).grid(row=3,column=4)

# Costos paraciales de cada vehículo
parciales = f"\nBarcos:$ {barcoCosto}\nTren:$ {trenCosto}\nAvion:$ {avionCosto}\nCamion:$ {camionCosto}"

# Label de costo
labelCostoTotal = Label(root, text=f"Costo Total:$ {monto} Pesos", bg="gold2", width=30, height=2, font=("Arial",12,'bold')).grid(row=6,column=1)
labelTotalesP= Label(root, text=f"Total Costos Parciales: {parciales}", bg="gold1", width=30, height=5, font=("Arial",12,'bold')).grid(row=6,column=2)

# Bucle principal de la interfaz gráfica
root.mainloop()