from tkinter import *

root=Tk()
root.title("Calculadora")
frame0=Frame(root)
frame0.pack()
operacion=""
resultado=0
#var_pantalla------------
numeroPantalla=StringVar()
#Pantalla---------------
pantalla= Entry(frame0,textvariable=numeroPantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",fg="white",justify="right")
#Numero Pantalla----------
def numeroPulsado(num):
    global operacion
    if(operacion!=""):
        numeroPantalla.set(num)
        operacion=""
    else:
        numeroPantalla.set(numeroPantalla.get()+num)
#suma
def suma(num):
    global operacion
    global resultado
    operacion="suma"
    resultado+=float(num)
    numeroPantalla.set(resultado)
#igual
def resultado_total():
    global resultado
    numeroPantalla.set(resultado+float(numeroPantalla.get()))
    resultado=0

#Fila1----------------------------------------
boton7=Button(frame0,text="7",width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(frame0,text="8",width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(frame0,text="9",width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=3)
botonDiv=Button(frame0,text="/",width=3)
botonDiv.grid(row=2,column=4)
#Fila2---------------------------------------
boton4=Button(frame0,text="4",width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(frame0,text="5",width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(frame0,text="6",width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMul=Button(frame0,text="*",width=3)
botonMul.grid(row=3,column=4)
#Fila3---------------------------------------
boton1=Button(frame0,text="1",width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(frame0,text="2",width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(frame0,text="3",width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4,column=3)
botonRes=Button(frame0,text="-",width=3)
botonRes.grid(row=4,column=4)
#Fila4---------------------------------------
botonpto=Button(frame0,text=".",width=3,command=lambda:numeroPulsado("."))
botonpto.grid(row=5,column=1)
boton0=Button(frame0,text="0",width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=2)
botonequ=Button(frame0,text="=",width=3,command=lambda:resultado_total())
botonequ.grid(row=5,column=3)
botonSum=Button(frame0,text="+",width=3,command=lambda:suma(numeroPantalla.get()))
botonSum.grid(row=5,column=4)



root.mainloop()