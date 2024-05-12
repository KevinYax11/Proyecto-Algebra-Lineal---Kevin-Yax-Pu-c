import tkinter as tk
from tkinter import ttk, scrolledtext

def obtener_matriz(texto):
    filas = texto.split("\n")
    matriz = []
    for fila in filas:
        elementos = fila.split(",")
        fila_matriz = [float(elemento) for elemento in elementos if elemento]
        matriz.append(fila_matriz)
    return matriz

def eliminar_filas_ceros(matriz):
    matriz_sin_ceros = []
    for fila in matriz:
        if any(elemento != 0 for elemento in fila):
            matriz_sin_ceros.append(fila)
    return matriz_sin_ceros

def eliminar_columnas_ceros(matriz):
    transposicion = list(map(list, zip(*matriz)))
    transposicion_sin_ceros = eliminar_filas_ceros(transposicion)
    matriz_sin_ceros = list(map(list, zip(*transposicion_sin_ceros)))
    return matriz_sin_ceros

def convertir_forma_escalon(matriz):
    filas_matriz = len(matriz)
    columnas_matriz = len(matriz[0])

    for i in range(filas_matriz):
        if all(matriz[i][j] == 0 for j in range(columnas_matriz)):
            continue

        pivote = matriz[i][matriz[i].index(next(elemento for elemento in matriz[i] if elemento != 0))]
        for j in range(i + 1, filas_matriz):
            factor = matriz[j][matriz[i].index(pivote)] / pivote
            for k in range(columnas_matriz):
                matriz[j][k] -= factor * matriz[i][k]
    return matriz

def calcular_rango(matriz):
    matriz = eliminar_filas_ceros(matriz)
    matriz = eliminar_columnas_ceros(matriz)
    matriz = convertir_forma_escalon(matriz)
    rango = len(matriz)
    for fila in matriz:
        if all(elemento == 0 for elemento in fila):
            rango -= 1
    return rango

def determinar_rango():
    matriz = obtener_matriz(entrada_matriz.get("1.0", "end-1c"))
    rango = calcular_rango(matriz)
    area_resultado.delete("1.0", tk.END)
    area_resultado.insert(tk.END, f"El rango de la matriz es: {rango}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo del Rango de una Matriz")

# Crear etiquetas y campos de entrada
etiqueta_matriz = ttk.Label(ventana, text="Ingrese la matriz:")
etiqueta_matriz.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

entrada_matriz = scrolledtext.ScrolledText(ventana, width=30, height=5)
entrada_matriz.grid(row=0, column=1, padx=5, pady=5)

etiqueta_resultado = ttk.Label(ventana, text="Rango de la matriz:")
etiqueta_resultado.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

area_resultado = scrolledtext.ScrolledText(ventana, width=30, height=1)
area_resultado.grid(row=1, column=1, padx=5, pady=5)

# Crear botón para calcular el rango
boton_calcular = ttk.Button(ventana, text="Calcular Rango", command=determinar_rango)
boton_calcular.grid(row=2, column=1, padx=5, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()