from tkinter import Tk,Frame,StringVar,Entry,Button,Label,Spinbox,messagebox,Text,Scrollbar,INSERT,END
from tkinter import ttk
import psycopg2 as ps

class aerolinea(Frame):

    def __init__(self,master):
        super().__init__(master)
        self.master.title("Aerolinea")
        self.grid(row=1,column=1)
        self.frame_0=Frame(self.master)                 #Etiquetas de seleccion de precios
        self.frame_0.grid(row=4,column=1)
        self.frame_1=Frame(self.master)              #precios
        self.frame_1.grid(row=2,column=1)
        self.frame_2=Frame(self.master)                 #Botones
        self.frame_2.grid(row=6,column=1)
        self.frame_3=Frame(self.master)               #Tabla
        self.frame_3.grid(row=1,column=2,rowspan=6)
        self.frame_4=Frame(self.master)  #Entrada de nombre y seleccion de clase
        self.frame_4.grid(row=3,column=1)
        self.tableVar=StringVar()
        self.subTotal=StringVar()
        self.desc=StringVar()
        self.toTal=StringVar()
        self.nombreVar=StringVar()
        #
        self.com1clss=StringVar()
        self.beb1clss=StringVar()
        self.pel1clss=StringVar()
        #
        self.com2clss=StringVar()
        self.beb2clss=StringVar()
        self.pel2clss=StringVar()
        #
        self.com3clss=StringVar()
        self.beb3clss=StringVar()
        self.pel3clss=StringVar()
        #
        self.clssVuelo=StringVar()
        self.label()
        self.spinbox()
        self.button()
        self.entry()
        self.combobox()
#        self.text()
        self.subTotal.set("0")
        self.nombreVar.set("")
        self.desc.set("0")
        self.toTal.set("0")
        self.tableVar.set("columna 1 /n columna 2  ")
        self.text_0=Text(self.frame_3)
        self.text_0.grid(row=1,column=1)
        self.scrollvertical = Scrollbar(self.frame_3,command=self.text_0.yview)
        self.scrollvertical.grid(row=1,column=2,sticky="nsew")
        self.text_0.config(yscrollcommand=self.scrollvertical.set)
#        self.text_0.insert(INSERT,"prueba\n")

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
        self.clssg=Label(self.frame_4,text="Clase de vuelo",padx=10, pady=5).grid(row=2,column=1)
        self.nombre=Label(self.frame_4,text="Nombre",padx=10,pady=5).grid(row=1,column=1)
        #-------subtotal, descuento y total--------------
        self.subtotal=Label(self.frame_0,text="Subtotal",padx=10,pady=5).grid(row=6,column=1,columnspan=2)
        self.Descuento=Label(self.frame_0,text="Descuento",padx=10,pady=5).grid(row=7,column=1,columnspan=2)
        self.Total=Label(self.frame_0,text="Total",padx=10,pady=5).grid(row=8,column=1,columnspan=2)
    
    def spinbox(self):
        #-----Selectores de cantidad--------------------------------------------------
        self.clss1Comida=Spinbox(self.frame_0,textvariable=self.com1clss,from_=0,to=30,state="readonly",width=2).grid(row=3,column=2)
        self.clss1Bebida=Spinbox(self.frame_0,textvariable=self.beb1clss,from_=0,to=30,state="readonly",width=2).grid(row=3,column=3)
        self.clss1Pelicula=Spinbox(self.frame_0,textvariable=self.pel1clss,from_=0,to=30,state="readonly",width=2).grid(row=3,column=4)
        #
        self.clss2Comida=Spinbox(self.frame_0,textvariable=self.com2clss,from_=0,to=30,state="readonly",width=2).grid(row=4,column=2)
        self.clss2Bebida=Spinbox(self.frame_0,textvariable=self.beb2clss,from_=0,to=30,state="readonly",width=2).grid(row=4,column=3)
        self.clss2Pelicula=Spinbox(self.frame_0,textvariable=self.pel2clss,from_=0,to=30,state="readonly",width=2).grid(row=4,column=4)
        #
        self.clss3Comida=Spinbox(self.frame_0,textvariable=self.com3clss,from_=0,to=30,state="readonly",width=2).grid(row=5,column=2)
        self.clss3Bebida=Spinbox(self.frame_0,textvariable=self.beb3clss,from_=0,to=30,state="readonly",width=2).grid(row=5,column=3)
        self.clss3Pelicula=Spinbox(self.frame_0,textvariable=self.pel3clss,from_=0,to=30,state="readonly",width=2).grid(row=5,column=4)
        #
    def combobox(self): 
        clssOpc=["","1","2","3"]
        self.clssopc=ttk.Combobox(self.frame_4,values=clssOpc,textvariable=self.clssVuelo,state="readonly",width=2).grid(row=2,column=2)

    def button(self):
        self.button_0=Button(self.frame_2,text="Limpiar",command=self.limpiar).grid(row=1,column=1)
        self.button_1=Button(self.frame_2,text="Salir",command=self.master.destroy).grid(row=1,column=2)
        self.button_2=Button(self.frame_2,text="Reporte",command=self.postgres_select).grid(row=1,column=3)
        self.button_3=Button(self.frame_2,text="Calcular",command=self.calc).grid(row=1,column=4)    

    def entry(self):
        self.entryNombre=Entry(self.frame_4,textvariable=self.nombreVar).grid(row=1,column=2) #Entrada de nombre   
        self.sub_total=Entry(self.frame_0,textvariable=self.subTotal,state="disable",width=6).grid(row=6,column=3,columnspan=2)
        self.descuento_0=Entry(self.frame_0,textvariable=self.desc,width=6).grid(row=7,column=3,columnspan=2)
        self.total_0=Entry(self.frame_0,textvariable=self.toTal,width=6).grid(row=8,column=3,columnspan=2)

    def limpiar(self):
        self.nombreVar.set("")#Variable de nombre
        #
        self.com1clss.set("0")#Variable de cantidad de comida 1 clase
        self.beb1clss.set("0")#Variable de cantidad de bebida 1 clase
        self.pel1clss.set("0")#Variable de cantidad de pelicula 1 clase
        #
        self.com2clss.set("0")#Variable de cantidad de comida 2 clase
        self.beb2clss.set("0")#Variable de cantidad de bebida 2 clase
        self.pel2clss.set("0")#Variable de cantidad de pelicula 2 clase
        #
        self.com3clss.set("0")#Variable de cantidad de comida 3 clase
        self.beb3clss.set("0")#Variable de cantidad de bebida 3 clase
        self.pel3clss.set("0")#Variable de cantidad de pelicula 3 clase
        #        
        self.subTotal.set("0")#Subtotal
        self.desc.set("0")    #Descuento
        self.toTal.set("0")   #Total
        #
        self.clssVuelo.set("")
        self.text_0.delete(1.0,END)
    
    def postgres_insert(self,nombre,vuelo,clss1,clss2,clss3,subTotal,descuento,total):
        conexion=None
        try:
            conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="192.168.1.74",port="5432")
            cursor=conexion.cursor()
            cursor.execute("""INSERT INTO public."boletosAerolinea"("ID", nombre, "claseVuelo", "cantClase1", "cantClase2", "cantClase3", subtotal, descuento, total)
            VALUES (nextval('pk_boletosAerolinea'), %(nm)s, %(clssV)s, %(cntClss1)s, %(cntClss2)s
            , %(cntClss3)s,%(sub)s,%(des)s,%(total)s); """,{'nm':nombre,'clssV':vuelo ,'cntClss1':clss1 ,'cntClss2':clss2 ,'cntClss3':clss3,'sub':subTotal,'des':descuento,'total':total})
            conexion.commit()
            cursor.close()
        except (Exception, ps.Error) as error:
            print("Error al obtener datos ", error)
        finally:
            if conexion is not None:
                conexion.close()

    def postgres_select(self):
        self.text_0.delete(1.0,END)
        conexion=None
        try:
            conexion=ps.connect(database="Parcial2",user="postgres",password="123456",host="192.168.1.74",port="5432")
            cursor=conexion.cursor()
            cursor.execute("""SELECT "ID","nombre",subtotal,descuento,total  FROM public."boletosAerolinea" ORDER BY "ID" ASC""")
            datos=cursor.fetchall()
            print("-------------------------------Registro-----------------------------")
            for fila in datos:
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                print("ID: ",fila[0])
                print("Nombre: ",fila[1])
                print("Subtotal: ",fila[2])
                print("Descuento: ",fila[3])
                print("Total: ",fila[4])
                print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                cursor.close()
                print("--------------------------------------------------------------------")
        #Parte de Tkinter
            self.text_0.insert(INSERT,"ID\tNOMBRE\tSUBTOTAL\tDESCUENTO\tTOTAL\n")
            for fila in datos:
                self.text_0.insert(INSERT,"_______________________________________________________________________\n")
                self.text_0.insert(INSERT,"{}\t{}\t{}\t{}\t{}\n".format(fila[0],fila[1],fila[2],fila[3],fila[4]))
        except (Exception, ps.Error) as error:
            print("Error al obtener datos ", error)
        finally:
            if(conexion is not None):
                conexion.close()

    def calc(self):
        try:
            if(self.nombreVar.get()==""):
                messagebox.showerror("Error","Nombre vacio")
            elif(self.clssVuelo.get()==""):
                messagebox.showerror("Error","No se ha seleccionado una clase de vuelo")
            else:
                Descuento=0
                cntServicios=0
                clssVuelo=int(self.clssVuelo.get())
                clssBebida=[int(self.beb1clss.get()),int(self.beb2clss.get()),int(self.beb3clss.get())]
                clssComida=[int(self.com1clss.get()),int(self.com2clss.get()),int(self.com3clss.get())]
                clssPelicula=[int(self.pel1clss.get()),int(self.pel2clss.get()),int(self.pel3clss.get())]
                for cnt in clssBebida:
                    cntServicios=cntServicios+cnt
                for cnt in clssComida:
                    cntServicios=cntServicios+cnt 
                for cnt in clssPelicula:
                    cntServicios=cntServicios+cnt
                subtotal=50*clssComida[0]+40*clssComida[1]+25*clssComida[2]+35*clssBebida[0]+25*clssBebida[1]+10*clssBebida[2]+70*clssPelicula[0]+55*clssPelicula[1]+25*clssPelicula[2]
                if(cntServicios>=10):
                    Descuento= 0.1*subtotal
                elif(clssVuelo==1 and clssBebida[1]==clssBebida[2]==clssComida[1]==clssComida[2]==clssPelicula[1]==clssPelicula[2]==0 and clssBebida[0]>=1 and clssComida[0]>=1 and clssPelicula[0]>=1):
                    Descuento= 0.05*subtotal
                else:
                    Descuento=0
                cntServicios1=clssBebida[0]+clssComida[0]+clssPelicula[0]
                cntServicios2=clssBebida[1]+clssComida[1]+clssPelicula[1]
                cntServicios3=clssBebida[2]+clssComida[2]+clssPelicula[2]
                Total=subtotal-Descuento
                self.subTotal.set(str(subtotal)+".00")
                self.desc.set(str(Descuento))
                self.toTal.set(str(Total))
                self.postgres_insert(self.nombreVar.get(),
                                clssVuelo,
                                cntServicios1,
                                cntServicios2,
                                cntServicios3,
                                subtotal,
                                Descuento,
                                Total)
        except Exception as exc:
            print(str(exc)+"\n Algo va mal")

root=Tk()
aer=aerolinea(root)
aer.mainloop()