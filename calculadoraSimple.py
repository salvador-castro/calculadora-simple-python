import tkinter as tk
from tkinter import messagebox

# Lista para almacenar el historial
historial = []

# Función que maneja los clics en los botones
def on_button_click(value):
    if value == "C":
        entry.delete(0, tk.END)  # Borra todo el contenido de la entrada
    elif value == "=":
        try:
            expression = entry.get().replace(",", ".")  # Reemplazar coma por punto
            
            if "/0" in expression:  # Detectar división por cero
                raise ZeroDivisionError
            
            result = eval(expression)  # Evaluar la expresión matemática

            # Convertir a entero si el resultado no tiene decimales
            if result == int(result):
                result = int(result)

            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))  # Mostrar el resultado

            # Guardar la operación en el historial
            historial.append(f"{expression.replace('.', ',')} = {str(result).replace('.', ',')}")
            actualizar_historial()

        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")
        except Exception:
            messagebox.showerror("Error", "Expresión inválida")  # Manejo de errores generales
    else:
        # Evitar múltiples puntos/comas en un mismo número
        if value in [",", "."]:
            last_char = entry.get()[-1:]  # Último carácter ingresado
            if last_char in [",", "."]:  # Evita ingresar dos comas seguidas
                return
        entry.insert(tk.END, value)  # Agregar número u operador al campo de entrada

# Función para manejar la entrada desde el teclado
def key_press(event):
    key = event.char
    if key in "0123456789+-*/=,.":
        on_button_click(key)
    elif key == "\r":  # Enter para calcular
        on_button_click("=")
    elif key == "\x08":  # Backspace para borrar
        entry.delete(len(entry.get()) - 1, tk.END)

# Función para actualizar el historial de operaciones
def actualizar_historial():
    historial_text.config(state=tk.NORMAL)  # Habilitar edición temporal
    historial_text.delete(1.0, tk.END)  # Limpiar historial anterior
    for operacion in historial[-5:]:  # Mostrar solo las últimas 5 operaciones
        historial_text.insert(tk.END, operacion + "\n")
    historial_text.config(state=tk.DISABLED)  # Deshabilitar edición

# Función para borrar el historial
def borrar_historial():
    global historial
    historial = []  # Limpiar la lista del historial
    actualizar_historial()

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("300x500")
root.resizable(False, False)

# Pantalla de entrada
entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.SUNKEN)
entry.pack(pady=10, fill="both")

# Botones de la calculadora (ahora con ",")
buttons = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", ",", "+"),
    ("=")
]

frame = tk.Frame(root)
frame.pack()

for row in buttons:
    row_frame = tk.Frame(frame)
    row_frame.pack(expand=True, fill="both")

    for btn_text in row:
        btn = tk.Button(row_frame, text=btn_text, font=("Arial", 15), height=2, width=5,
                        command=lambda txt=btn_text: on_button_click(txt))
        btn.pack(side="left", expand=True, fill="both")

# Área de historial
historial_label = tk.Label(root, text="Historial", font=("Arial", 12, "bold"))
historial_label.pack(pady=5)

historial_text = tk.Text(root, height=5, font=("Arial", 10), state=tk.DISABLED)
historial_text.pack(padx=10, pady=5, fill="both")

# Botón para borrar el historial
borrar_historial_btn = tk.Button(root, text="Borrar Historial", font=("Arial", 12), command=borrar_historial)
borrar_historial_btn.pack(pady=5, fill="both")

# Configurar entrada de teclado
root.bind("<Key>", key_press)

# Ejecutar la aplicación
root.mainloop()
