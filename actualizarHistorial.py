import tkinter as tk  # ✅ Importar tkinter

def actualizar_historial(historial_text, historial):
    """Actualiza el historial de operaciones en la interfaz."""
    
    # ✅ Verificar que historial_text no sea None antes de modificarlo
    if historial_text is None:
        return  # Si es None, no hacer nada

    historial_text.config(state=tk.NORMAL)  # Habilitar edición temporal
    historial_text.delete(1.0, tk.END)  # Limpiar historial anterior
    for operacion in historial[-5:]:  # Mostrar solo las últimas 5 operaciones
        historial_text.insert(tk.END, operacion + "\n")
    historial_text.config(state=tk.DISABLED)  # Deshabilitar edición
