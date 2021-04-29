import tkinter as tk
from tkinter import ttk
 
app = tk.Tk() 
app.geometry('200x100')

spinbox0=tk.Spinbox(app,from_=0,to=10,state="readonly")
spinbox0.pack()

print(spinbox0.get(),type(spinbox0.get()))

app.mainloop()