import tkinter as tk

def saludar():
    nombre=txtNombre.get()
    apodo=txtApodo.get()
    lblScreen.config(text=f"Su nombre es: {nombre}  {apodo}")  
def limpiar():
    lblScreen.config(text="")
    txtNombre.delete(0,tk.END)
    txtApodo.delete(0,tk.END)

ventana=tk.Tk()
ventana.title("BIENVENIDO")
ventana.geometry("400x400")
txtNombre=tk.Entry()
lblnombre=tk.Label(text="INGRESE SU NOMBRE: ")
txtApodo=tk.Entry()
lblApodo=tk.Label(text="INGRESE SU APODO: ")

btnOK=tk.Button(text="SALUDAR",command=saludar)
btnLimpiar=tk.Button(text="LIMPIAR",command=limpiar)
lblScreen=tk.Label()


lblnombre.pack()
txtNombre.pack()
lblApodo.pack()
txtApodo.pack()
btnOK.pack()
btnLimpiar.pack()
lblScreen.pack()
ventana.mainloop()