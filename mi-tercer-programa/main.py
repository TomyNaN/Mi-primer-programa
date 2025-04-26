import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi primera interfaz")
ventana.geometry("400x300")

#crear una casilla de tick
casilla_tick = tk.Checkbutton(ventana, text="Tarea 1", command=lambda: print("¡Tarea 1 completada!")) 
casilla_tick.pack(pady=10)

# Variable para el tiempo
contador = 10

# Función para actualizar el temporizador
def actualizar_tiempo():
    global contador
    if contador > 0:
        etiqueta.config(text=f"Tiempo restante: {contador} segundos")
        contador -= 1
        ventana.after(1000, actualizar_tiempo)  # Llama a esta función después de 1 segundo
    else:
        etiqueta.config(text="¡Tiempo terminado!")

# Etiqueta para mostrar el tiempo
etiqueta = tk.Label(ventana, text=f"Tiempo restante: {contador} segundos", font=("Arial", 14))
etiqueta.pack(pady=20)

# Botón para iniciar el temporizador
boton = tk.Button(ventana, text="Iniciar", command=actualizar_tiempo)
boton.pack(pady=10)

# Ejecutar el bucle principal
ventana.mainloop()