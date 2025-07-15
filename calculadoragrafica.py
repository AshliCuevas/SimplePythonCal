from tkinter import *
from math import *

#funciones de los botones
def presionar(valor):
    actual = salida.get()
    salida.delete(0, END)
    salida.insert(0, str(actual) + str(valor))

def calcular():
    try:
        resultado = eval(salida.get())
        salida.delete(0, END)
        salida.insert(0, str(resultado))
    except Exception as e:
        salida.delete(0, END)
        salida.insert(0, "Error")

def limpiar():
    salida.delete(0, END)
    
    
# Crear la ventana principal
ventana = Tk()
ventana.title("Calculadora")
ventana.config(bg="white") 
ventana.geometry("500x400")

#Se crea los datos de los botones
ancho_boton = 10
alto_boton = 2

#creamos los botones
Button(ventana, text="0", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(0)).place(x=150, y=260)
Button(ventana, text="1", width=ancho_boton, height=alto_boton, bg="lightpink",command=lambda: presionar(1)).place(x=50, y=200)
Button(ventana, text="2", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(2)).place(x=150, y=200)
Button(ventana, text="3", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(3)).place(x=250, y=200)
Button(ventana, text="4", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(4)).place(x=50, y=140)
Button(ventana, text="5", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(5)).place(x=150, y=140)
Button(ventana, text="6", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(6)).place(x=250, y=140)
Button(ventana, text="7", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(7)).place(x=50, y=80)
Button(ventana, text="8", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(8)).place(x=150, y=80)
Button(ventana, text="9", width=ancho_boton, height=alto_boton, bg="lightpink", command=lambda: presionar(9)).place(x=250, y=80)

#ventana de salida
salida = Entry(ventana, font=("Arial", 22, "bold"), width = 22, bd=10, justify="right", bg="white")
salida.place (x=50, y=10)    

#creamos los botones de operaciones
boton_suma = Button(ventana, text="+", width=ancho_boton, height=alto_boton, command=lambda:presionar("+")).place(x=350, y= 80)
boton_resta = Button(ventana, text="-", width=ancho_boton, height=alto_boton, command=lambda:presionar("-")).place(x=350, y= 140)
boton_multiplicacion = Button(ventana, text="*", width=ancho_boton, height=alto_boton, command=lambda:presionar("*")).place(x=350, y= 200)
boton_division = Button(ventana, text="/", width=ancho_boton, height=alto_boton, command=lambda:presionar("/")).place(x=350, y= 260)
boton_igual = Button(ventana, text="=", width=ancho_boton, height=alto_boton, bg="lightgreen", command=calcular).place(x=250, y=260)
boton_limpiar = Button(ventana, text="C", width=ancho_boton, height=alto_boton, bg="lightcoral", command=limpiar).place(x=50, y=260)

#creamos el boton de salir
boton_salir = Button(ventana, text="Salir", width=ancho_boton, height=alto_boton, bg="white", command=ventana.quit).place(x=400, y=320)

# Iniciamos el bucle principal de la ventana
ventana.resizable(0, 0)  # Evita que la ventana se pueda redimensionar


ventana.mainloop()
