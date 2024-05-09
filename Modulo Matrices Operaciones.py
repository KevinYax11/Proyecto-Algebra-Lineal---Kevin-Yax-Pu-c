import tkinter as tk
from tkinter import ttk, scrolledtext

def obtener_dimensiones(matriz):
    filas = 0
    columnas = 0

    for fila in matriz:
        filas += 1
        columnas = 0
        for elemento in fila:
            columnas += 1

    return filas, columnas

def sumar_matrices(A, B):
    filas_A, columnas_A = obtener_dimensiones(A)
    filas_B, columnas_B = obtener_dimensiones(B)

    if filas_A != filas_B or columnas_A != columnas_B:
        return "Las matrices no tienen las mismas dimensiones"

    C = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_A):
            fila.append(A[i][j] + B[i][j])
        C.append(fila)

    return C

def restar_matrices(A, B):
    filas_A, columnas_A = obtener_dimensiones(A)
    filas_B, columnas_B = obtener_dimensiones(B)

    if filas_A != filas_B or columnas_A != columnas_B:
        return "Las matrices no tienen las mismas dimensiones"

    C = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_A):
            fila.append(A[i][j] - B[i][j])
        C.append(fila)

    return C

def multiplicar_matrices(A, B):
    filas_A, columnas_A = obtener_dimensiones(A)
    filas_B, columnas_B = obtener_dimensiones(B)

    if columnas_A != filas_B:
        return "Las dimensiones de las matrices no son compatibles para la multiplicación"

    C = []
    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma += A[i][k] * B[k][j]
            fila.append(suma)
        C.append(fila)

    return C

def producto_punto(A, B):
    filas_A, columnas_A = obtener_dimensiones(A)
    filas_B, columnas_B = obtener_dimensiones(B)

    if filas_A != filas_B or columnas_A != columnas_B:
        return "Las matrices no tienen las mismas dimensiones"

    suma = 0
    for i in range(filas_A):
        for j in range(columnas_A):
            suma += A[i][j] * B[i][j]

    return suma

def realizar_operacion():
    operacion = operaciones.get()
    matriz_a = obtener_matriz(entrada_matriz_a.get("1.0", "end-1c"))
    matriz_b = obtener_matriz(entrada_matriz_b.get("1.0", "end-1c"))

    if operacion == "Suma":
        resultado = sumar_matrices(matriz_a, matriz_b)
    elif operacion == "Resta":
        resultado = restar_matrices(matriz_a, matriz_b)
    elif operacion == "Multiplicación":
        resultado = multiplicar_matrices(matriz_a, matriz_b)
    elif operacion == "Producto punto":
        resultado = producto_punto(matriz_a, matriz_b)
    else:
        resultado = "Operación inválida"

    area_resultado.delete("1.0", tk.END)
    area_resultado.insert(tk.END, str(resultado))

def obtener_matriz(texto):
    filas = texto.split("\n")
    matriz = []
    for fila in filas:
        elementos = fila.split(",")
        fila_matriz = [int(elemento) for elemento in elementos]
        matriz.append(fila_matriz)
    return matriz

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Operaciones con Matrices")
ventana.geometry("450x450")

# Crear etiquetas y campos de entrada
etiqueta_operacion = ttk.Label(ventana, text="Operación:")
etiqueta_operacion.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

operaciones = tk.StringVar()
combo_operaciones = ttk.Combobox(ventana, textvariable=operaciones, values=["Suma", "Resta", "Multiplicación", "Producto punto"])
combo_operaciones.grid(row=0, column=1, padx=5, pady=5)

etiqueta_matriz_a = ttk.Label(ventana, text="Matriz A:")
etiqueta_matriz_a.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

entrada_matriz_a = scrolledtext.ScrolledText(ventana, width=30, height=5)
entrada_matriz_a.grid(row=1, column=1, padx=5, pady=5)

etiqueta_matriz_b = ttk.Label(ventana, text="Matriz B:")
etiqueta_matriz_b.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

entrada_matriz_b = scrolledtext.ScrolledText(ventana, width=30, height=5)
entrada_matriz_b.grid(row=2, column=1, padx=5, pady=5)

etiqueta_resultado = ttk.Label(ventana, text="Resultado:")
etiqueta_resultado.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

area_resultado = scrolledtext.ScrolledText(ventana, width=30, height=5)
area_resultado.grid(row=3, column=1, padx=5, pady=5)

# Crear botón para realizar la operación
boton_calcular = ttk.Button(ventana, text="Calcular", command=realizar_operacion)
boton_calcular.grid(row=4, column=1, padx=5, pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()