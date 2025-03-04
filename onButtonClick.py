import tkinter as tk
from actualizarHistorial import actualizar_historial
from tkinter import messagebox

def on_button_click(value, entry, historial_text=None, historial=None):
    """Maneja los clics en los botones de la calculadora."""

    # ✅ Asegurar que historial no sea None
    if historial is None:
        historial = []

    if value == "C":
        entry.delete(0, tk.END)  # Borra todo el contenido de la entrada
    elif value == "=":
        try:
            expression = entry.get().strip().replace(",", ".")  # ✅ Limpia la entrada
            
            # Verifica que la expresión no esté vacía o termine en un operador
            if not expression or expression[-1] in "+-*/":
                raise ValueError("Expresión incompleta")

            result = eval(expression)  # Evaluar la expresión matemática

            # Convertir a entero si el resultado no tiene decimales
            if result == int(result):
                result = int(result)

            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))  # Mostrar el resultado

            # ✅ Si historial_text es None, no intentar actualizarlo
            if historial_text is not None:
                historial.append(f"{expression.replace('.', ',')} = {str(result).replace('.', ',')}")
                actualizar_historial(historial_text, historial)

        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")
        except ValueError:
            messagebox.showerror("Error", "Expresión inválida")
        except Exception as e:
            messagebox.showerror("Error", f"Expresión inválida: {e}")
    else:
        # Evitar múltiples puntos/comas en un mismo número
        if value in [",", "."]:
            last_char = entry.get()[-1:]  # Último carácter ingresado
            if last_char in [",", "."]:  # Evita ingresar dos comas seguidas
                return
        entry.insert(tk.END, value)  # ✅ Agregar número u operador al campo de entrada correctamente