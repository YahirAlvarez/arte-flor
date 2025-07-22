from turtle import *       # Módulo de dibujo tipo "tortuga"
import colorsys            # Módulo para manejar colores en formato HSV

# Configuración inicial de la pantalla
bgcolor('black')           # Color de fondo: negro
pensize(4)                 # Grosor de la línea
tracer(10)                 # Aumenta la velocidad del dibujo (menos animación)
h = 0                      # Inicializa el tono de color HSV (Hue)

# Función personalizada de dibujo con dos arcos
def dibujo(a, n):
    # Dibuja dos arcos simétricos de radio 5+n y ángulo 60°
    circle(5 + n, 60)
    left(a)                # Gira la tortuga a la izquierda "a" grados
    circle(5 + n, 60)

# Bucle principal para dibujar el patrón
for i in range(360):
    # Genera un color RGB desde el modelo HSV (hue, saturation, value)
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.008             # Incrementa el tono para el siguiente color

    # Establece color de línea y relleno
    color(c, 'black')
    begin_fill()           # Comienza a rellenar la figura
    dibujo(90, i / 2)      # Dibujo con ángulo 90° y tamaño variable
    end_fill()             # Finaliza el relleno

    dibujo(160, i * 1.2)   # Dibujo adicional con ángulo 160° y tamaño creciente
    penup()                # Levanta el lápiz para mover sin dibujar
    dibujo(0, 0)           # Reposiciona la tortuga
    dibujo(90, i / 2)      # Redibuja simétricamente
    pendown()              # Baja el lápiz para volver a dibujar

# Termina el dibujo y mantiene la ventana abierta
done()