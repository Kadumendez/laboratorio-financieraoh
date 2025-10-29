# Laboratorio: Tarjeta OH

## ID de Historia

OH-TARJ-001

## Perfil del Usuario

Como **analista programador en Financiera OH**, se le ha encargado implementar un servicio REST de evaluación crediticia para clientes potenciales que van a solicitar su primera **Tarjeta OH**.
El objetivo es automatizar la validación de requisitos mínimos y asignar una categoría de tarjeta según la capacidad del cliente, utilizando un algorítmo que será detallado a continuación.

## Tarea Asignada

Usted, como analista programador, se le ha asignado la siguiente historia de Financiera OH con **8 puntos de esfuerzo**.
Los detalles son los siguientes:

- Implementar una ruta REST en la API de FastAPI bajo el path `/evaluaciones/tarjetas`.
- Esta ruta recibirá dos parámetros: `edad` e `ingresos`.
- La lógica de negocio estará separada en un archivo independiente (`scoring.py`) para permitir pruebas unitarias.
- El endpoint deberá llamar al módulo y retornar un JSON estandarizado.
- Como institución bancaria, estamos siguiendo normas ISO, que determinan que debemos mantener un **test coverage de al menos 90%** en los componentes críticos de software.

---

## Detalles del Algoritmo de Evaluación

Reglas de negocio:

1. **Edad mínima**: 18 años.
2. **Ingresos mínimos**: S/ 1000.
3. Si no cumple edad o ingresos → **Rechazado**.
4. Si cumple requisitos:
   - Ingresos menores a S/ 5000 → **Tarjeta OH**, línea máxima aprobada: S/ 2000.
   - Ingresos mayores o iguales a S/ 5000 y edad mayor o igual a 25 → **Tarjeta OH Premium**, línea máxima aprobada: S/ 10000.
5. En cualquier otro caso intermedio (ejemplo: ingresos altos pero edad menor a 25) → **Tarjeta OH regular** con línea de S/ 2000.
