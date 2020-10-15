class ComplexForDummies:
    """
    Class ComplexForDummies
    """

    def __init__(self, re: float, im: float):
        self._re = re
        self._im = im

    def module(self) -> float:
        return (self._re ** 2 + self._im ** 2) ** 0.5

    @property
    def re(self):
        return self._re

    @re.setter
    def re(self, value):
        self._re = value

    @property
    def im(self):
        return self._im

    @im.setter
    def im(self, value):
        self._im = value

    def conjugate(self):
        return ComplexForDummies(self.re, - self.im)

    def add(self, c2):
        return ComplexForDummies(self.re + c2.re, self.im + c2.im)

    pass
