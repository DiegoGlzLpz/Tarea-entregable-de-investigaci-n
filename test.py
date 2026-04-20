import pytest
from main import comprobarPar,quitarEspacios,hacerCuadrado

@pytest.mark.basic


def test_comprobarPar():
    assert (comprobarPar(4)==True and comprobarPar(5)==False) 


def test_quitarEspacios():
    assert quitarEspacios("Texto de prueba")=="Textodeprueba"


def test_hacerCuadrado():
    assert (hacerCuadrado(4)==16 and hacerCuadrado(21)==441)