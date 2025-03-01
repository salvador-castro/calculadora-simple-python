# Calculadora con Historial y Soporte para Decimales en Python

Este proyecto es una calculadora de escritorio desarrollada en **Python** utilizando la biblioteca **Tkinter** para la interfaz gráfica. Incluye funcionalidades avanzadas como un historial de operaciones y soporte para ingresar decimales usando tanto **coma** (`,`) como **punto** (`.`).

## Características Principales

✅ **Interfaz intuitiva y responsiva** con botones grandes.\
✅ **Soporte para teclado** (permite ingresar números y operadores desde el teclado).\
✅ **Historial de operaciones** (se muestran las últimas 5 operaciones realizadas).\
✅ **Soporte para decimales con **``** y **`` (convierte `,` a `.` automáticamente para evaluación).\
✅ **Evita errores como la división por cero** y expresiones inválidas.\
✅ **Botón para borrar el historial** y limpiar los registros.

---

## Instalación y Uso

### 1. Requisitos previos

Para ejecutar esta calculadora, necesitas tener instalado **Python 3** en tu sistema.

Puedes verificar si Python está instalado ejecutando:

```sh
python --version
```

### 2. Clonar el Repositorio

```sh
git clone https://github.com/tu_usuario/calculadora-tkinter.git
cd calculadora-tkinter
```

### 3. Ejecutar el Programa

Ejecuta el siguiente comando en la terminal o en un entorno de desarrollo (VSCode, PyCharm, etc.):

```sh
python calculadora.py
```

---

## Explicación del Código

El programa se divide en varias secciones clave:

1. **Interfaz Gráfica con Tkinter**:

   - Se crea una ventana principal (`Tk`) con un campo de entrada (`Entry`) para mostrar las operaciones y resultados.
   - Se agregan botones para los números, operadores y funciones especiales.

2. **Lógica de Cálculo**:

   - Se reemplaza `,` por `.` para la evaluación de la expresión.
   - Se usa `eval()` para calcular el resultado.
   - Se manejan errores como división por cero y expresiones inválidas.

3. **Historial de Operaciones**:

   - Se almacena en una lista y se muestran las últimas 5 operaciones.
   - Se usa un `Text` deshabilitado para evitar ediciones accidentales.
   - Se permite borrar el historial con un botón.

4. **Soporte para Teclado**:

   - Se permite la entrada de números y operadores con el teclado.
   - `Enter` realiza el cálculo y `Backspace` borra caracteres.

---

## Mejoras Futuras

🔹 Agregar un **modo oscuro** para mejorar la visualización.\
🔹 Implementar **operaciones avanzadas** como raíces y potencias.\
🔹 Crear un instalador ejecutable para facilitar el uso sin Python.

---

## Licencia

Este proyecto está bajo la licencia **MIT**, por lo que puedes usarlo y modificarlo libremente.

Si te gustó este proyecto, ¡no olvides darle una estrella en GitHub! ⭐

