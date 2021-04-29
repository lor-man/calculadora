from tkinter import Tk, Frame,StringVar, Entry, Button

class Calculadora(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        #self.master=master
        self.pack()
        self.master.title("Calculadora")
        self.operacion=""
        self.resultado=0
        self.numeroPantalla=StringVar()
        self.frame0=Frame(self.master)
        self.frame0.pack()
        self.pantalla()
        self.botones()

    def pantalla(self):
        self.pantalla=Entry(self.frame0,textvariable=self.numeroPantalla)
        self.pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
        self.pantalla.config(background="black",fg="white",justify="right")
    def botones(self):
        #Fila1----------------------------------------
        self.boton7=Button(self.frame0,text="7",width=3,command=lambda:self.numeroPulsado("7"))
        self.boton7.grid(row=2,column=1)
        self.boton8=Button(self.frame0,text="8",width=3,command=lambda:self.numeroPulsado("8"))
        self.boton8.grid(row=2,column=2)
        self.boton9=Button(self.frame0,text="9",width=3,command=lambda:self.numeroPulsado("9"))
        self.boton9.grid(row=2,column=3)
        self.botonDiv=Button(self.frame0,text="/",width=3)
        self.botonDiv.grid(row=2,column=4)
    #Fila2---------------------------------------
        self.boton4=Button(self.frame0,text="4",width=3,command=lambda:self.numeroPulsado("4"))
        self.boton4.grid(row=3,column=1)
        self.boton5=Button(self.frame0,text="5",width=3,command=lambda:self.numeroPulsado("5"))
        self.boton5.grid(row=3,column=2)
        self.boton6=Button(self.frame0,text="6",width=3,command=lambda:self.numeroPulsado("6"))
        self.boton6.grid(row=3,column=3)
        self.botonMul=Button(self.frame0,text="*",width=3)
        self.botonMul.grid(row=3,column=4)
        #Fila3---------------------------------------
        self.boton1=Button(self.frame0,text="1",width=3,command=lambda:self.numeroPulsado("1"))
        self.boton1.grid(row=4,column=1)
        self.boton2=Button(self.frame0,text="2",width=3,command=lambda:self.numeroPulsado("2"))
        self.boton2.grid(row=4,column=2)
        self.boton3=Button(self.frame0,text="3",width=3,command=lambda:self.numeroPulsado("3"))
        self.boton3.grid(row=4,column=3)
        self.botonRes=Button(self.frame0,text="-",width=3)
        self.botonRes.grid(row=4,column=4)
        #Fila4---------------------------------------
        self.botonpto=Button(self.frame0,text=".",width=3,command=lambda:self.numeroPulsado("."))
        self.botonpto.grid(row=5,column=1)
        self.boton0=Button(self.frame0,text="0",width=3,command=lambda:self.numeroPulsado("0"))
        self.boton0.grid(row=5,column=2)
        self.botonequ=Button(self.frame0,text="=",width=3,command=lambda:self.resultado_total())
        self.botonequ.grid(row=5,column=3)
        self.botonSum=Button(self.frame0,text="+",width=3,command=lambda:self.suma(self.numeroPantalla.get()))
        self.botonSum.grid(row=5,column=4)
    
    def numeroPulsado(self,num):
        if(self.operacion!=""):
            self.numeroPantalla.set(num)
            self.operacion=""
        else:
            self.numeroPantalla.set(self.numeroPantalla.get()+num)

    def suma(self,num):
        self.operacion="suma"
        self.resultado+=float(num)
        self.numeroPantalla.set(self.resultado)

    def resultado_total(self):
        self.numeroPantalla.set(self.resultado+float(self.numeroPantalla.get()))
        self.resultado=0

       
root=Tk()
cal=Calculadora(root)
cal.mainloop()