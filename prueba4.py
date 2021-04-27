from tkinter import *

class Calculadora(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.master.title("Calculadora")
        self.operacion=""
        self.resutlado=0
        self.numeroPantalla=StringVar()
        self.frame0=Frame(self.master)
        self.frame0.pack()
        self.pantalla()

    def pantalla(self):
        self.pantalla=Entry(self.frame0,textvariable=self.numeroPantalla)
        self.pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
        self.pantalla.config(background="black",fg="white",justify="right")

        
       
root=Tk()
cal=Calculadora(root)
cal.mainloop()