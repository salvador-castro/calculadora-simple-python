import tkinter as tk
from tkinter import messagebox
from actualizarHistorial import actualizar_historial
from borrarHistorial import borrar_historial
from keyPress import key_press
from onButtonClick import on_button_click

# Lista para almacenar el historial
historial = []

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x500")
root.resizable(False, False)

# Pantalla de entrada
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.SUNKEN)
entry.pack(pady=10, fill="both")

# Botones de la calculadora (con "," en lugar de ".")
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", ",", "+"),
    ("=")
]

frame = tk.Frame(root)
frame.pack()

# ✅ Crear los botones asegurando que se pasa historial y historial_text correctamente
for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn_text in row:
        btn = tk.Button(
            row_frame, text=btn_text, font=("Arial", 15), height=2, width=5,
            command=lambda txt=btn_text: on_button_click(txt, entry, historial_text, historial)  # ✅ Pasar historial y historial_text
        )
        btn.pack(side="left", expand=True, fill="both")

# Área de historial
historial_label = tk.Label(root, text="Historial", font=("Arial", 12, "bold"))
historial_label.pack(pady=5)

historial_text = tk.Text(root, height=5, font=("Arial", 10), state=tk.DISABLED)
historial_text.pack(padx=10, pady=5, fill="both")

# Botón para borrar el historial
borrar_historial_btn = tk.Button(
    root, text="Borrar Historial", font=("Arial", 12), 
    command=lambda: borrar_historial(historial, historial_text)  # ✅ Pasar historial y historial_text
)
borrar_historial_btn.pack(pady=5, fill="both")

# Configurar entrada de teclado
root.bind("<Key>", lambda event: key_press(event, entry))  # ✅ Pasar solo event y entry

# Ejecutar la aplicación
root.mainloop()