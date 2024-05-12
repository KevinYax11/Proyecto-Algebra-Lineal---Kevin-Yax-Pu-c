import tkinter as tk
from tkinter import ttk, scrolledtext

def es_matriz_cuadrada(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    return filas == columnas

def determinante(matriz):
    n = len(matriz)
    if n == 1:
        return matriz[0][0]
    elif n == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for j in range(n):
            submatriz = [fila[:j] + fila[j+1:] for fila in matriz[1:]]
            det += matriz[0][j] * (-1)**j * determinante(submatriz)
        return det


def obtener_matriz(texto):
    filas = texto.split("\n")
    matriz = []
    for fila in filas:
        elementos = fila.split(",")
        fila_matriz = []
        for elemento in elementos:
            if elemento.strip():  # Verifica si el elemento no está vacío después de eliminar espacios
                fila_matriz.append(float(elemento))
        if fila_matriz:  # Añade la fila solo si no está vacía
            matriz.append(fila_matriz)
    return matriz

def calcular_determinante():
    matriz = obtener_matriz(entrada_matriz.get("1.0", "end-1c"))
    if es_matriz_cuadrada(matriz):
        det = determinante(matriz)
        area_resultado.delete("1.0", tk.END)
        area_resultado.insert(tk.END, str(det))
    else:
        area_resultado.delete("1.0", tk.END)
        area_resultado.insert(tk.END, "La matriz no es cuadrada")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo del Determinante")

# Crear etiquetas y campos de entrada
etiqueta_matriz = ttk.Label(ventana, text="Ingrese la matriz:")
etiqueta_matriz.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entrada_matriz = scrolledtext.ScrolledText(ventana, width=30, height=5)
entrada_matriz.grid(row=0, column=1, padx=5, pady=5)

etiqueta_resultado = ttk.Label(ventana, text="Determinante:")
etiqueta_resultado.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

area_resultado = scrolledtext.ScrolledText(ventana, width=30, height=1)
area_resultado.grid(row=1, column=1, padx=5, pady=5)

# Crear botón para calcular el determinante
boton_calcular = ttk.Button(ventana, text="Calcular Determinante", command=calcular_determinante)
boton_calcular.grid(row=2, column=1, padx=5, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
