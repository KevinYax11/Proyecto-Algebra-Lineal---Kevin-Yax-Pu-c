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
            det += matriz[0][j] * (-1)**(j) * determinante(submatriz)
        return det

def matriz_adjunta(matriz):
    n = len(matriz)
    adjunta = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            submatriz = [fila[:j] + fila[j+1:] for fila in (matriz[:i] + matriz[i+1:])]
            adjunta[i][j] = (-1)**(i+j) * determinante(submatriz)

    return adjunta

def matriz_inversa(matriz):
    if not es_matriz_cuadrada(matriz):
        return "La matriz no es cuadrada"

    det = determinante(matriz)
    if det == 0:
        return "La matriz no tiene inversa (determinante es 0)"

    adjunta = matriz_adjunta(matriz)
    inversa = [[elemento / det for elemento in fila] for fila in zip(*adjunta)]

    return inversa

def obtener_matriz(texto):
    filas = texto.split("\n")
    matriz = []
    for fila in filas:
        elementos = fila.split(",")
        fila_matriz = [float(elemento) for elemento in elementos if elemento]
        matriz.append(fila_matriz)
    return matriz

def calcular_inversa():
    matriz = obtener_matriz(entrada_matriz.get("1.0", "end-1c"))
    inversa = matriz_inversa(matriz)

    if isinstance(inversa, list):
        resultado = ""
        for fila in inversa:
            resultado += ", ".join(f"{elemento:.4f}" for elemento in fila) + "\n"
        area_resultado.delete("1.0", tk.END)
        area_resultado.insert(tk.END, resultado.strip())
    else:
        area_resultado.delete("1.0", tk.END)
        area_resultado.insert(tk.END, inversa)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Matriz Inversa")

# Crear etiquetas y campos de entrada
etiqueta_matriz = ttk.Label(ventana, text="Ingrese la matriz:")
etiqueta_matriz.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entrada_matriz = scrolledtext.ScrolledText(ventana, width=30, height=5)
entrada_matriz.grid(row=0, column=1, padx=5, pady=5)

etiqueta_resultado = ttk.Label(ventana, text="Inversa de la matriz:")
etiqueta_resultado.grid(rrow=1, column=0, padx=5, pady=5, sticky=tk.W)

area_resultado = scrolledtext.ScrolledText(ventana, width=30, height=5)
area_resultado.grid(row=1, column=1, padx=5, pady=5)

# Crear botón para calcular la inversa
boton_calcular = ttk.Button(ventana, text="Calcular Inversa", command=calcular_inversa)
boton_calcular.grid(row=2, column=1, padx=5, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()