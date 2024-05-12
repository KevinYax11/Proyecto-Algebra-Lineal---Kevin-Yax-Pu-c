import tkinter as tk
from tkinter import ttk
import subprocess

def abrir_operaciones_matrices():
    global frame_operaciones
    frame_operaciones = ttk.Frame(root, padding="30")  # Define el Frame globalmente
    frame_operaciones.grid(row=2, column=0, columnspan=2, pady=10)
    subprocess.Popen(["python", "Modulo Matrices Operaciones.py", str(frame_operaciones)])

def main():
    global root  # Define root globalmente
    root = tk.Tk()
    root.title("Interfaz de Operaciones entre Matrices")

    frame = ttk.Frame(root, padding="30")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    label = ttk.Label(frame, text="¡Bienvenido a la interfaz de operaciones entre matrices!", font=("Arial", 14))
    label.grid(row=0, column=0, columnspan=2, pady=10)

    btn_operaciones = ttk.Button(frame, text="Operaciones entre matrices", command=abrir_operaciones_matrices)
    btn_operaciones.grid(row=1, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
