# CAPA DE VALIDACIÓN: Lectura segura con try/except para evitar caídas por ValueError

def leer_texto_no_vacio(mensaje: str) -> str:
    """Solicita un texto por consola y repite mientras el usuario lo deje en blanco."""
    while True:
        valor = input(mensaje).strip()
        if len(valor) > 0:
            return valor
        print("Error: Este campo no puede quedar vacío. Intente nuevamente.")

def leer_entero_no_negativo(mensaje: str) -> int:
    """Solicita un número entero >= 0 usando try/except para evitar caídas por letras."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor >= 0:
                return valor
            print("Error: La cantidad no puede ser negativa. Ingrese un valor mayor o igual a 0.")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero válido.")

def leer_entero_positivo(mensaje: str) -> int:
    """Solicita un número entero estrictamente mayor a 0 (> 0) con manejo de excepciones."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Error: El valor debe ser mayor a cero. Intente nuevamente.")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un número entero válido.")

def leer_flotante_positivo(mensaje: str) -> float:
    """Solicita un precio decimal estrictamente mayor a 0.0 (> 0) con try/except."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0.0:
                return round(valor, 2)
            print("Error: El precio debe ser mayor a $0.00. Intente nuevamente.")
        except ValueError:
            print("Error: Entrada inválida. Debe ingresar un valor numérico (Ej. 12.50).")

def leer_opcion_rango(mensaje: str, minimo: int, maximo: int) -> int:
    """Solicita una opción entera dentro de un rango específico [minimo, maximo]."""
    while True:
        try:
            opcion = int(input(mensaje))
            if minimo <= opcion <= maximo:
                return opcion
            print(f"Error: Seleccione un número válido entre {minimo} y {maximo}.")
        except ValueError:
            print("Error: Entrada inválida. Ingrese únicamente el número de la opción.")