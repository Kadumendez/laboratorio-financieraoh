from fastapi import FastAPI, HTTPException
from califica import evaluar_cliente

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/evaluaciones/tarjetas")
def evaluarTarjetaCredito(edad: int, ingresos: float):
    if edad < 0 or ingresos < 0:
        raise HTTPException(status_code=400, detail="Datos Invalidos")

    resultado = evaluar_cliente(edad, ingresos)
    if resultado["aprobado"]:
        return {
            "status": "Aprobado",
            "mensaje": f"Aprobado para nuestro producto de : {resultado['categoria']} ",
            "data": resultado
        }
    else:
        return {
            "status": "Rechazado",
            "mensaje": "No cumple con los requisitos minimos para ser aprobado",
            "data": resultado
        }
