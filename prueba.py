from tkinter import Tk, Frame, Entry,Label,Text,Scrollbar, Button,StringVar
root=Tk()
root.title("Login")
minombre=StringVar()

frame0= Frame(root,width=1200,height=600)
frame0.pack()

entryNombre=Entry(frame0,textvariable=minombre)
entryNombre.grid(row=0,column=1, padx=10,pady=10)

entryApellido=Entry(frame0)
entryApellido.grid(row=1,column=1, padx=10,pady=10)

entryPass= Entry(frame0)
entryPass.grid(row=2,column=1, padx=10,pady=10)
entryPass.config(show="*")

entryDireccion= Entry(frame0)
entryDireccion.grid(row=3,column=1, padx=10,pady=10)

textComentario=Text(frame0,width=16,height=5)
textComentario.grid(row=4,column=1, padx=10,pady=10)


scrollB=Scrollbar(frame0,command=textComentario.yview)
scrollB.grid(row=4,column=2,sticky="nsew")
textComentario.config(yscrollcommand=scrollB.set)

labelNombre=Label(frame0,text="Nombre:")
labelNombre.grid(row=0,column=0, padx=10,pady=10)

labelApellido=Label(frame0,text="Apellido:")
labelApellido.grid(row=1,column=0, padx=10,pady=10)

labelPass=Label(frame0,text="Contraseña:")
labelPass.grid(row=2,column=0, padx=10,pady=10)

labelDireccion=Label(frame0,text="Direccion:")
labelDireccion.grid(row=3,column=0, padx=10,pady=10)

labelComentario=Label(frame0,text="Comentario")
labelComentario.grid(row=4,column=0,padx=10,pady=10)

def funcBoton():
    minombre.set("Omar")


bton=Button(root,text="Enviar",command=funcBoton)
bton.pack()

root.mainloop()
