from actualizarHistorial import actualizar_historial

def borrar_historial(historial, historial_text):
    """Borra el historial de operaciones."""
    historial.clear()  # Vacía la lista del historial
    actualizar_historial(historial_text, historial)  # Actualiza la interfaz
