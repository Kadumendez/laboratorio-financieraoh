# Lógica para evaluar la elegibilidad de un cliente para una tarjeta de crédito

def evaluar_cliente(edad: int, ingresos: float) -> dict:
    if edad < 18 or ingresos < 1000:
        return {"aprobado": False, "categoria": None, "linea": None}

    if ingresos >= 5000 and edad >= 25:
        return {"aprobado": True, "categoria": "Tarjeta Oh Premium", "linea": 10000}

    return {"aprobado": True, "categoria": "Tarjeta Oh", "linea": 2000}
