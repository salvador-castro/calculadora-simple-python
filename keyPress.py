import tkinter as tk  # ✅ Importar tkinter
from onButtonClick import on_button_click

def key_press(event, entry):
    """ Maneja la entrada de teclado en la calculadora. """
    key = event.char
    if key in "0123456789+-*/=,.":
        on_button_click(key, entry, None, None)  # ✅ Pasa solo entry (historial no es necesario)
    elif key == "\r":  # Enter para calcular
        on_button_click("=", entry, None, None)
    elif key == "\x08":  # Backspace para borrar
        entry.delete(len(entry.get()) - 1, tk.END)
