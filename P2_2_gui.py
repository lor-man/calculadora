from tkinter import Tk,Frame,StringVar,Entry,Button,Label,Spinbox

class aerolinea(Frame):
    def __init__(self,master):
        super().__init__(master)
        #self.pack()
        self.grid(row=1,column=1)
        self.master.title("Aerolinea")
        self.frame_1=Frame(self.master)
        self.frame_1.grid(row=1,column=1)
        self.frame_0=Frame(self.master)
        self.frame_0.grid(row=2,column=1)
        self.frame_2=Frame(self.master)
        self.frame_2.grid(row=4,column=1)
        self.frame_3=Frame(self.master)
        self.frame_3.grid(row=3,column=1)
        self.label()
        self.spinbox()
        self.button()
    
    def label(self):
        #------Cuadro de precios-------------------------------------
        #------Etiquetas de arriba-----------------------------------
        self.comida0=Label(self.frame_1,text="Comida",padx=10,pady=5)
        self.comida0.grid(row=1,column=2)
        self.bebida0=Label(self.frame_1,text="Bebida",padx=10,pady=5)
        self.bebida0.grid(row=1,column=3)
        self.pelicula0=Label(self.frame_1,text="Pelicula",padx=10,pady=5)
        self.pelicula0.grid(row=1,column=4)
        #------Etiquetas_Izquierda------------------------------------------------
        self.clss10=Label(self.frame_1,text="Clase/Tipo de servicio",padx=10,pady=5)
        self.clss10.grid(row=1,column=1)
        self.clss10=Label(self.frame_1,text="Clase 1",padx=10,pady=5)
        self.clss10.grid(row=3,column=1)
        self.clss20=Label(self.frame_1,text="Clase 2",padx=10,pady=5)
        self.clss20.grid(row=4,column=1)
        self.clss30=Label(self.frame_1,text="Clase 3",padx=10,pady=5)
        self.clss30.grid(row=5,column=1)
        #------Etiquetas_arriba---------------------------------------------------
        self.comida=Label(self.frame_0,text="Comida",padx=10,pady=5)
        self.comida.grid(row=1,column=2)
        self.bebida=Label(self.frame_0,text="Bebida",padx=10,pady=5)
        self.bebida.grid(row=1,column=3)
        self.pelicula=Label(self.frame_0,text="Pelicula",padx=10,pady=5)
        self.pelicula.grid(row=1,column=4)
        #------Etiquetas_Izquierda------------------------------------------------
        self.clss1=Label(self.frame_0,text="Clase/Tipo de servicio",padx=10,pady=5)
        self.clss1.grid(row=1,column=1)
        self.clss1=Label(self.frame_0,text="Clase 1",padx=10,pady=5)
        self.clss1.grid(row=3,column=1)
        self.clss2=Label(self.frame_0,text="Clase 2",padx=10,pady=5)
        self.clss2.grid(row=4,column=1)
        self.clss3=Label(self.frame_0,text="Clase 3",padx=10,pady=5)
        self.clss3.grid(row=5,column=1)
    
    def spinbox(self):
        #-----Selectores de cantidad--------------------------------------------------
        self.clss1Comida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss1Comida.grid(row=3,column=2)
        self.clss1Bebida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss1Bebida.grid(row=3,column=3)
        self.clss1Pelicula=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss1Pelicula.grid(row=3,column=4)
        #
        self.clss2Comida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss2Comida.grid(row=4,column=2)
        self.clss2Bebida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss2Bebida.grid(row=4,column=3)
        self.clss2Pelicula=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss2Pelicula.grid(row=4,column=4)
        #
        self.clss3Comida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss3Comida.grid(row=5,column=2)
        self.clss3Bebida=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss3Bebida.grid(row=5,column=3)
        self.clss3Pelicula=Spinbox(self.frame_0,from_=0,to=30,state="readonly",width=2)
        self.clss3Pelicula.grid(row=5,column=4)
    def button(self):
        self.button_0=Button(self.frame_2,text="Boton 0")
        self.button_0.grid(row=1,column=1)
        self.button_1=Button(self.frame_2,text="Boton 1")
        self.button_1.grid(row=1,column=2)
        self.button_2=Button(self.frame_2,text="Boton 2")
        self.button_2.grid(row=1,column=3)
        self.button_3=Button(self.frame_2,text="Boton 3")
        self.button_3.grid(row=1,column=4)    
        


root=Tk()
aer=aerolinea(root)
aer.mainloop()