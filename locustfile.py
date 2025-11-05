from locust import HttpUser, TaskSet, task, between
import random


# Endpoint de "Hola Mundo"
class HolaMundo(HttpUser):
    # cada usurario del test de carga esperará entre 1 y 3 segundos entre tareas
    host = "http://127.0.0.1:8000"
    wait_time = between(1, 3)

    @task
    def get_hola_mundo(self):
        # Realiza una solicitud GET a la ruta raíz del servidor
        self.client.get("/")


# Endpoint de /evaluaciones/tarjetas

class EvaluacionesTarjetas(HttpUser):

    # cada usuario del test de carga esperará entre 1 y 3 segundos entre tareas
    wait_time = between(1, 3)
    grupo_de_edades = [7, 15, 19, 25, 50, 60, 70]
    grupo_de_ingresos = [500, 1000, 2000, 4000, 5500, 7500]

    @task(80)
    def get_evaluaciones_tarjetas(self):
        # Realiza una solicitud GET a la ruta /evaluaciones/tarjetas

        edad = random.choice(self.grupo_de_edades)
        ingresos = random.choice(self.grupo_de_ingresos)

        self.client.get("/evaluaciones/tarjetas",
                        params={"edad": edad, "ingresos": ingresos})

    @task(20)
    def get_evaluaciones_tarjetas_invalidos(self):
        # Realiza una solicitud GET a la ruta /evaluaciones/tarjetas con datos inválidos
        with self.client.get("/evaluaciones/tarjetas",
                             params={"edad": -5, "ingresos": -1000}, catch_response=True) as response:

            if response.status_code == 400:
                response.success()
            else:
                response.failure(
                    f"Expected status code 400 but got {response.status_code}")
