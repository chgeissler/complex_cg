from complex import ComplexForDummies
import math


def test_i():
    i = ComplexForDummies.i()
    assert i * i == ComplexForDummies(-1)


def test_ipi():
    i = ComplexForDummies.i()
    pi = ComplexForDummies(math.pi)
    euler = (i * pi).exp()
    assert euler != ComplexForDummies(-1)
    assert euler.almost_eq(ComplexForDummies(-1))
