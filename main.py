from distutils.dist import command_re
from tkinter import Tk, Button, Entry
def insertar_numero(numero):
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]==" ":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(),str(numero))

# Operaciones aritmeticas
def igual():
    operacion=pantalla.get()
    if len(operacion.split("+"))==2:
        lista=operacion.split("+")
        prueba=comprobar_numeros(lista)
        if prueba:
            num1=cast_a_float(float(lista[0]))
            num2=cast_a_float(float(lista[1]))
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), num1+num2)
    elif len(operacion.split("/"))==2:
        lista=operacion.split("/")
        prueba=comprobar_numeros(lista)
        if prueba:
            num1=cast_a_float(float(lista[0]))
            num2=cast_a_float(float(lista[1]))
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), num1/num2)
    elif len(operacion.split("-"))==2:
        lista=operacion.split("-")
        prueba=comprobar_numeros(lista)
        if prueba:
            num1=cast_a_float(float(lista[0]))
            num2=cast_a_float(float(lista[1]))
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), num1-num2)
    elif len(operacion.split("*"))==2:
        lista=operacion.split("*")
        prueba=comprobar_numeros(lista)
        if prueba:
            num1=cast_a_float(float(lista[0]))
            num2=cast_a_float(float(lista[1]))
            pantalla.delete(0,pantalla.get().__len__()+1)
            pantalla.insert(pantalla.get().__len__(), num1*num2)
    else:
        pantalla.delete(0,pantalla.get().__len__()+1)
        pantalla.insert(pantalla.get().__len__(), "Error")
    if pantalla.get()!="Error":
        pantalla.insert(pantalla.get().__len__(), " ")

def suma():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]==" ":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "+")

def resta():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]==" ":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "-")

def multiplicacion():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]==" ":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "*")

def division():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]==" ":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), "/")

def punto():
    if pantalla.get()=="Error":
        pantalla.delete(0,pantalla.get().__len__()+1)
    if len(pantalla.get())>0:
        if pantalla.get()[len(pantalla.get())-1]==" ":
            pantalla.delete(0,pantalla.get().__len__()+1)
    pantalla.insert(pantalla.get().__len__(), ".")

def comprobar_numeros(lista):
    try:
        for x in lista: p = float(x)
    except ValueError:
        pantalla.delete(0, pantalla.get().__len__() + 1)
        pantalla.insert(pantalla.get().__len__(), "Error")
        return False
    return True

def cast_a_float(numero):
    if numero.is_integer(): return int(numero)
    else: return numero
# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry()

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=4, padx=1, pady=1)

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(1)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(2)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(3)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(4)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(5)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(6)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(7)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(8)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2", command=lambda: insertar_numero(9)).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor=" hand2", command=igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2", borderwidth=0, command=punto).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=suma).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=resta).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=multiplicacion).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2", command=division).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()