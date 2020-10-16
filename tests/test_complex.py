from complex import ComplexForDummies


def test_module():
    i = ComplexForDummies.i()
    assert i * i == ComplexForDummies(-1)
