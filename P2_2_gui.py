from tkinter import Tk,Frame,StringVar,Entry,Button,Label,Spinbox
from tkinter import ttk

class aerolinea(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.master.title("Aerolinea")
        self.grid(row=1,column=1)
        self.frame_0=Frame(self.master)                 #Etiquetas de seleccion de precios
        self.frame_0.grid(row=3,column=1)
        self.frame_1=Frame(self.master)              #precios
        self.frame_1.grid(row=1,column=1)
        self.frame_2=Frame(self.master)                 #Botones
        self.frame_2.grid(row=5,column=1)
        self.frame_3=Frame(self.master)               #Tabla
        self.frame_3.grid(row=4,column=1)
        self.frame_4=Frame(self.master)  #Entrada de nombre y seleccion de clase
        self.frame_4.grid(row=2,column=1)
        self.subTotal=StringVar()
        self.desc=StringVar()
        self.toTal=StringVar()
        self.label()
        self.spinbox()
        self.button()
        self.entry()
        self.combobox()
        self.subTotal.set("0")
        self.desc.set("0")
        self.toTal.set("0")
        
    
    def label(self):
        #------Cuadro de precios-------------------------------------
        #------Etiquetas de arriba-----------------------------------
        self.precios=Label(self.frame_1,text="Precios",padx=10,pady=5).grid(row=1,column=1,columnspan=4)
        self.comida0=Label(self.frame_1,text="Comida",padx=10,pady=5).grid(row=2,column=2)
        self.bebida0=Label(self.frame_1,text="Bebida",padx=10,pady=5).grid(row=2,column=3)
        self.pelicula0=Label(self.frame_1,text="Pelicula",padx=10,pady=5).grid(row=2,column=4)
        #------Etiquetas_Izquierda------------------------------------------------
        self.clss10=Label(self.frame_1,text="Clase/Tipo de servicio",padx=10,pady=5).grid(row=2,column=1)
        self.clss10=Label(self.frame_1,text="Clase 1",padx=10,pady=5).grid(row=3,column=1)
        self.clss20=Label(self.frame_1,text="Clase 2",padx=10,pady=5).grid(row=4,column=1)
        self.clss30=Label(self.frame_1,text="Clase 3",padx=10,pady=5).grid(row=5,column=1)
        #------Precios-----------------------------------
        self.clss1Comida0=Label(self.frame_1,text="50").grid(row=3,column=2)
        self.clss2Comida0=Label(self.frame_1,text="40").grid(row=3,column=3)
        self.clss3Comida0=Label(self.frame_1,text="25").grid(row=3,column=4)
        #
        self.clss1Bebida0=Label(self.frame_1,text="35").grid(row=4,column=2)
        self.clss1Bebida1=Label(self.frame_1,text="25").grid(row=4,column=3)
        self.clss1Bebida2=Label(self.frame_1,text="10").grid(row=4,column=4)
        #
        self.clss1Pelicula0=Label(self.frame_1,text="70").grid(row=5,column=2)
        self.clss1Pelicula1=Label(self.frame_1,text="55").grid(row=5,column=3)
        self.clss1Pelicula2=Label(self.frame_1,text="25").grid(row=5,column=4)
        #------Etiquetas_arriba---------------------------------------------------
        self.comida=Label(self.frame_0,text="Comida",padx=10,pady=5).grid(row=1,column=2)
        self.bebida=Label(self.frame_0,text="Bebida",padx=10,pady=5).grid(row=1,column=3)
        self.pelicula=Label(self.frame_0,text="Pelicula",padx=10,pady=5).grid(row=1,column=4)
        #------Etiquetas_Izquierda------------------------------------------------
        self.clss1=Label(self.frame_0,text="Clase/Tipo de servicio",padx=10,pady=5).grid(row=1,column=1)
        self.clss1=Label(self.frame_0,text="Clase 1",padx=10,pady=5).grid(row=3,column=1)
        self.clss2=Label(self.frame_0,text="Clase 2",padx=10,pady=5).grid(row=4,column=1)
        self.clss3=Label(self.frame_0,text="Clase 3",padx=10,pady=5).grid(row=5,column=1)
        #-------Entrada de nombre y seleccion de clase
        self.clssg=Label(self.frame_4,text="Seleccione la clase de vuelo",padx=10, pady=5).grid(row=2,column=1)
        self.nombre=Label(self.frame_4,text="Ingrese su nombre",padx=10,pady=5).grid(row=1,column=1)
        #-------subtotal, descuento y total--------------
        self.subtotal=Label(self.frame_0,text="Subtotal",padx=10,pady=5).grid(row=6,column=1,columnspan=2)
        self.Descuento=Label(self.frame_0,text="Descuento",padx=10,pady=5).grid(row=7,column=1,columnspan=2)
        self.Total=Label(self.frame_0,text="Total",padx=10,pady=5).grid(row=8,column=1,columnspan=2)
    
    def spinbox(self):
        #-----Selectores de cantidad--------------------------------------------------
        self.clss1Comida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=3,column=2)
        self.clss1Bebida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=3,column=3)
        self.clss1Pelicula=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=3,column=4)
        #
        self.clss2Comida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=4,column=2)
        self.clss2Bebida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=4,column=3)
        self.clss2Pelicula=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=4,column=4)
        #
        self.clss3Comida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=5,column=2)
        self.clss3Bebida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=5,column=3)
        self.clss3Pelicula=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2).grid(row=5,column=4)
        #
    def combobox(self): 
        clssOpc=["","1","2","3"]
        self.clssopc=ttk.Combobox(self.frame_4,values=clssOpc,state="readonly").grid(row=2,column=2)


    def button(self):
        self.button_0=Button(self.frame_2,text="Limpiar").grid(row=1,column=1)
        self.button_1=Button(self.frame_2,text="Salir",command=self.master.destroy).grid(row=1,column=2)
        self.button_2=Button(self.frame_2,text="Reporte").grid(row=1,column=3)
        self.button_3=Button(self.frame_2,text="Calcular").grid(row=1,column=4)    

    def entry(self):
        self.entryNombre=Entry(self.frame_4).grid(row=1,column=2) #Entrada de nombre   
        self.sub_total=Entry(self.frame_0,textvariable=self.subTotal,state="disable").grid(row=6,column=3,columnspan=2)
        self.descuento_0=Entry(self.frame_0,textvariable=self.desc).grid(row=7,column=3,columnspan=2)
        self.total_0=Entry(self.frame_0,textvariable=self.toTal).grid(row=8,column=3,columnspan=2)


root=Tk()
aer=aerolinea(root)
aer.mainloop()