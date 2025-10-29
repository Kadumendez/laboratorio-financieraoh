from califica import evaluar_cliente

# edad: 17, ingresos: 2000


def test_cliente_menor_edad():
    resultado = evaluar_cliente(17, 2000)
    assert resultado["aprobado"] == False
    assert resultado["categoria"] == None

# edad: 19, ingresos: 900


def test_cliente_bajos_ingresos():
    resultado = evaluar_cliente(19, 900)
    assert resultado["aprobado"] == False


# Tarjeta Oh Regular
def test_oh_regular():
    resultado = evaluar_cliente(22, 2000)
    assert resultado["aprobado"] == True
    assert resultado["categoria"] == "Tarjeta Oh"


# Tarjeta Oh Premium


def test_oh_premium():
    resultado = evaluar_cliente(30, 5500)
    assert resultado["aprobado"] == True
    assert resultado["categoria"] == "Tarjeta Oh Premium"


# Tarjeta Oh Regular por Edad


def test_oh_regular_por_edad():
    resultado = evaluar_cliente(24, 6000)
    assert resultado["aprobado"] == True
    assert resultado["categoria"] == "Tarjeta Oh"
