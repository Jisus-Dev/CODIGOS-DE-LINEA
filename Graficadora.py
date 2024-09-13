import turtle
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Unipolar
class Unipolar:
    def __init__(self, señal: str):
        self.señal = señal
        self.alto_logico = 50
        self.bajo_logico = 0
        self.distancia = 50

    def dibujar(self):
        for i in self.señal:
            if i == '0':
                self.cero()
            elif i == '1':
                self.uno()

    def cero(self):
        t.sety(self.bajo_logico)
        t.forward(self.distancia)
        self.etiqueta(0)

    def uno(self):
        t.sety(self.alto_logico)
        t.forward(self.distancia)
        self.etiqueta(1)

    def etiqueta(self, valor):
        t.penup()
        t.setx(t.xcor() - self.distancia / 2)
        t.sety(t.ycor() - 18)
        t.write(valor, align="center", font=("Arial", 12, "normal"))
        t.sety(t.ycor() + 18)
        t.setx(t.xcor() + self.distancia / 2)
        t.pendown()

# NRZ-I : No Retorno a Cero (Invertido)
class NRZ_I:
    def __init__(self, señal: str):
        self.señal = señal
        self.alto_logico = 50
        self.bajo_logico = -50
        self.distancia = 50
        self.nivel_actual = self.bajo_logico

    def dibujar(self):
        for i in self.señal:
            if i == '0':
                self.cero()
            elif i == '1':
                self.uno()
    
    def cero(self):
        t.sety(self.nivel_actual)
        t.forward(self.distancia)
        self.etiqueta(0)
    
    def uno(self):
        self.nivel_actual = self.alto_logico if self.nivel_actual == self.bajo_logico else self.bajo_logico
        t.sety(self.nivel_actual)
        t.forward(self.distancia)
        self.etiqueta(1)
    
    def etiqueta(self, valor):
        t.penup()
        t.setx(t.xcor() - self.distancia / 2)
        t.sety(t.ycor() - 18)
        t.write(valor, align="center", font=("Arial", 12, "normal"))
        t.sety(t.ycor() + 18)
        t.setx(t.xcor() + self.distancia / 2)
        t.pendown()

# NRZ-L : No Retorno a Cero (Nivel)
class NRZ_L:
    def __init__(self, señal: str):
        self.señal = señal
        self.alto_logico = 50
        self.bajo_logico = -50
        self.distancia = 50

    def dibujar(self):
        for i in self.señal:
            if i == '0':
                self.cero()
            elif i == '1':
                self.uno()

    def cero(self):
        t.sety(self.bajo_logico)
        t.forward(self.distancia)
        self.etiqueta(0)

    def uno(self):
        t.sety(self.alto_logico)
        t.forward(self.distancia)
        self.etiqueta(1)

    def etiqueta(self, valor):
        t.penup()
        t.setx(t.xcor() - self.distancia / 2)
        t.sety(t.ycor() - 18)
        t.write(valor, align="center", font=("Arial", 12, "normal"))
        t.sety(t.ycor() + 18)
        t.setx(t.xcor() + self.distancia / 2)
        t.pendown()

# RZ : Retorno a Cero
class RZ:
    def __init__(self, señal: str):
        self.señal = señal
        self.alto_logico = 50
        self.bajo_logico = -50
        self.distancia = 50

    def dibujar(self):
        for i in self.señal:
            if i == '0':
                self.cero()
            elif i == '1':
                self.uno()

    def cero(self):
        t.sety(self.bajo_logico)
        t.forward(self.distancia / 2)
        t.sety(0)
        t.forward(self.distancia / 2)
        self.etiqueta(0)

    def uno(self):
        t.sety(self.alto_logico)
        t.forward(self.distancia / 2)
        t.sety(0)
        t.forward(self.distancia / 2)
        self.etiqueta(1)

    def etiqueta(self, valor):
        t.penup()
        t.setx(t.xcor() - (self.distancia / 2 + 10))
        t.sety(t.ycor() - 18)
        t.write(valor, align="center", font=("Arial", 12, "normal"))
        t.sety(t.ycor() + 18)
        t.setx(t.xcor() + (self.distancia / 2 + 10))
        t.pendown()

# Manchester
class Manchester:
    def __init__(self, señal: str):
        self.señal = señal
        self.alto_logico = 50
        self.bajo_logico = -50
        self.distancia = 50

    def dibujar(self):
        for i in self.señal:
            if i == '0':
                self.cero()
            elif i == '1':
                self.uno()

    def cero(self):
        t.sety(self.alto_logico)
        t.forward(self.distancia / 2)
        t.sety(self.bajo_logico)
        t.forward(self.distancia / 2)
        self.etiqueta(0,-18)

    def uno(self):
        t.sety(self.bajo_logico)
        t.forward(self.distancia / 2)
        t.sety(self.alto_logico)
        t.forward(self.distancia / 2)
        self.etiqueta(1,2)

    def etiqueta(self, valor,despl_vertical):
        t.penup()
        t.setx(t.xcor() - self.distancia / 2)
        t.sety(t.ycor() + despl_vertical)
        t.write(valor, align="center", font=("Arial", 12, "normal"))
        t.sety(t.ycor() - despl_vertical)
        t.setx(t.xcor() + self.distancia / 2)
        t.pendown()

# AMI : Inversión Alterna de Marcado
class AMI:
    def __init__(self, señal: str):
        self.señal = señal
        self.alto_logico = 50
        self.bajo_logico = -50
        self.distancia = 50
        self.base = 0
        self.polaridad_actual = self.bajo_logico

    def dibujar(self):
        for i in self.señal:
            if i == '0':
                self.cero()
            elif i == '1':
                self.uno()

    def cero(self):
        t.sety(self.base)
        t.forward(self.distancia)
        self.etiqueta(0)

    def uno(self):
        if self.polaridad_actual == self.bajo_logico:
            self.polaridad_actual = self.alto_logico
        else:
            self.polaridad_actual = self.bajo_logico
        
        t.sety(self.polaridad_actual)
        t.forward(self.distancia)
        self.etiqueta(1)

    def etiqueta(self, valor):
        t.penup()
        t.setx(t.xcor() - self.distancia / 2)
        t.sety(t.ycor() - 18)
        t.write(valor, align="center", font=("Arial", 12, "normal"))
        t.sety(t.ycor() + 18)
        t.setx(t.xcor() + self.distancia / 2)
        t.pendown()

# B8ZS : Bipolar con Sustitución de 8 Ceros
class B8ZS:
    def __init__(self, señal: str):
        self.señal = señal
        self.alto_logico = 50
        self.bajo_logico = -50
        self.distancia = 50
        self.base = 0
        self.polaridad_actual = self.bajo_logico
        self.señal_salida = self.aplicar_sustitucion_b8zs()

    def aplicar_sustitucion_b8zs(self):
        # Aplicar la sustitución B8ZS en la señal
        señal_salida = ''
        cuenta_ceros = 0
        for bit in self.señal:
            if bit == '0':
                cuenta_ceros += 1
            else:
                if cuenta_ceros == 8:
                    # Sustituir 8 ceros por la secuencia 000VB0VB
                    señal_salida += '0000'
                    señal_salida += self._b8zs_alternar_signos()
                    cuenta_ceros = 0
                señal_salida += '1'
                cuenta_ceros = 0
        if cuenta_ceros == 8:
            señal_salida += '0000'
            señal_salida += self._b8zs_alternar_signos()
        else:
            señal_salida += '0' * cuenta_ceros
        return señal_salida

    def _b8zs_alternar_signos(self):
        # Alternar entre +V y -V para la secuencia B8ZS
        if self.polaridad_actual == self.bajo_logico:
            self.polaridad_actual = self.alto_logico
            return '0'  # Alternar el signo para la secuencia B8ZS
        else:
            self.polaridad_actual = self.bajo_logico
            return '1'  # Alternar el signo para la secuencia B8ZS

    def dibujar(self):
        for i in self.señal_salida:
            if i == '0':
                self.cero()
            elif i == '1':
                self.uno()

    def cero(self):
        t.sety(self.base)
        t.forward(self.distancia)
        self.etiqueta(0)

    def uno(self):
        if self.polaridad_actual == self.bajo_logico:
            self.polaridad_actual = self.alto_logico
        else:
            self.polaridad_actual = self.bajo_logico
        
        t.sety(self.polaridad_actual)
        t.forward(self.distancia)
        self.etiqueta(1)

    def etiqueta(self, valor):
        t.penup()
        t.setx(t.xcor() - self.distancia / 2)
        t.sety(t.ycor() - 18)
        t.write(valor, align="center", font=("Arial", 12, "normal"))
        t.sety(t.ycor() + 18)
        t.setx(t.xcor() + self.distancia / 2)
        t.pendown()

def dibujar_ejes_y_rejilla(longitud_señal):
    altura_lienzo = 400
    espaciado_rejilla = 50
    
    t.pencolor("lightgray")
    t.penup()
    
    x_inicio = -370
    x_fin = x_inicio + len(longitud_señal) * espaciado_rejilla
    y_inicio = -altura_lienzo / 8
    y_fin = altura_lienzo / 8

    x = x_inicio
    while x <= x_fin:
        t.goto(x, y_inicio)
        t.pendown()
        t.goto(x, y_fin)
        t.penup()
        x += espaciado_rejilla

    t.goto(x_fin, y_inicio)
    t.pendown()
    t.goto(x_fin, y_fin)
    t.penup()

    y = y_inicio
    while y <= y_fin:
        t.goto(x_inicio, y)
        t.pendown()
        t.goto(x_fin, y)
        t.penup()
        y += espaciado_rejilla

    t.goto(x_inicio, y_fin)
    t.pendown()
    t.goto(x_fin, y_fin)
    t.penup()

    t.pencolor("gray")
    t.penup()
    t.goto(-370, 0)
    t.pendown()
    t.forward(len(longitud_señal) * espaciado_rejilla)
    
    t.penup()
    t.goto(-370, 0)
    t.left(90)
    t.pendown()
    t.forward(altura_lienzo / 4)
    t.backward(altura_lienzo / 2)
    t.right(90)
    t.penup()
    
    t.penup()
    t.goto(x_fin + 10, -10)
    t.write("X", align="left", font=("Arial", 12, "normal"))
    
    t.goto(-370, y_fin + 60)
    t.write("Y", align="center", font=("Arial", 12, "normal"))
    
    t.goto(-370, 0)
    t.pendown()

def dibujar_señal():
    # Deshabilitar el botón de graficar para multiples clics
    boton_graficar.config(state="disabled")
    
    t.clear()
    señal = entrada_señal.get()
    dibujar_ejes_y_rejilla(señal)
    
    # Obtener la señal y el tipo de codificación seleccionados
    tipo_codificacion = var_codificacion.get()
    
    # Verificar que la entrada sea una cadena binaria
    if not all(char in '01' for char in señal):
        messagebox.showerror("Error", "La señal debe contener solo caracteres 0 y 1.")
        return
    
    # Crear un objeto de la clase adecuada según la selección
    if tipo_codificacion == "Unipolar":
        codificador = Unipolar(señal)
    elif tipo_codificacion == "NRZ-I":
        codificador = NRZ_I(señal)
    elif tipo_codificacion == "NRZ-L":
        codificador = NRZ_L(señal)
    elif tipo_codificacion == "RZ":
        codificador = RZ(señal)
    elif tipo_codificacion == "Manchester":
        codificador = Manchester(señal)
    elif tipo_codificacion == "AMI":
        codificador = AMI(señal)
    elif tipo_codificacion == "B8ZS":
        codificador = B8ZS(señal)
    else:
        return
    
    # Mover la tortuga al origen
    t.penup()
    t.goto(-370, 0)
    t.setheading(0)
    t.pendown()
    
    # Alternar colores en la gráfica
    colores = ["red", "blue"]
    indice_color = 0
    
    # Dibujar la señal
    for i in señal:
        t.pencolor(colores[indice_color])
        if i == '0':
            codificador.cero()
        elif i == '1':
            codificador.uno()
        indice_color = 1 - indice_color  # Alternar el índice del color
    
    # Ajustar el rango del scroll según la longitud de la señal
    canvas.config(scrollregion=(-390, -150, -350 + len(señal) * 50, 150))
    
    # Habilitar el botón de graficar para nueva resolucion
    boton_graficar.config(state="normal")

# Configurar la ventana principal
root = tk.Tk()
root.title("Códigos de línea")

# Bloquear el redimensionamiento de la ventana (evitar errores visuales)
root.resizable(False, False)

# Obtener el tamaño de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Definir el tamaño de la ventana
ancho_ventana = 800
alto_ventana = 470

# Calcular la posición X e Y para centrar la ventana
pos_x = (ancho_pantalla - ancho_ventana) // 2
pos_y = (alto_pantalla - alto_ventana) // 2

# Establecer el tamaño y la posición de la ventana
root.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

# Crear un contenedor para el área de dibujo y el scrollbar
frame_canvas = tk.Frame(root)
frame_canvas.pack(fill=tk.BOTH, expand=True)

# Crear el scrollbar horizontal
scrollbar_horizontal = tk.Scrollbar(frame_canvas, orient=tk.HORIZONTAL)
scrollbar_horizontal.pack(side=tk.BOTTOM, fill=tk.X)

# Configurar el área de dibujo de Turtle con un scrollbar
canvas = tk.Canvas(frame_canvas, width=800, height=300, bg="white", scrollregion=(-370, -150, 2000, 150))
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Asociar el scrollbar con el canvas
canvas.config(xscrollcommand=scrollbar_horizontal.set)
scrollbar_horizontal.config(command=canvas.xview)

# Crear el objeto Turtle
pantalla = turtle.TurtleScreen(canvas)
pantalla.bgcolor("white")  # Establecer el fondo del lienzo a blanco
t = turtle.RawTurtle(pantalla)
t.speed(0)
t.hideturtle()  # Ocultar el cursor de Turtle

# Crear un marco para agrupar los controles
frame_controles = tk.Frame(root, bg="white", padx=300, pady=20)
frame_controles.pack(pady=0)

# Menú desplegable para seleccionar el tipo de codificación
var_codificacion = tk.StringVar()
var_codificacion.set("Unipolar")

etiqueta_codificacion = tk.Label(frame_controles, text="Seleccione el tipo de codificación:", bg="white")
etiqueta_codificacion.pack()

menu_codificacion = ttk.Combobox(frame_controles, textvariable=var_codificacion, state="readonly")
menu_codificacion['values'] = ("Unipolar", "NRZ-I", "NRZ-L", "RZ", "Manchester", "AMI", "B8ZS")
menu_codificacion.pack()

# Campo de entrada para la señal binaria
etiqueta_señal = tk.Label(frame_controles, text="Ingrese la señal binaria (solo 0s y 1s):", bg="white")
etiqueta_señal.pack()

# Ampliar el campo de entrada
entrada_señal = tk.Entry(frame_controles, width=100)  # Aumentar el ancho del campo de entrada
entrada_señal.pack()

# Botón para graficar la señal
boton_graficar = tk.Button(frame_controles, text="Graficar Señal", command=dibujar_señal)
boton_graficar.pack()

# Iniciar la interfaz gráfica
root.mainloop()