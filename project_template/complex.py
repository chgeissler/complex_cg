import math
import numpy as np


class ComplexForDummies:
    """
    Class ComplexForDummies
    """

    def __init__(self, re: float = 0.0, im: float = 0.0):
        self._re = re
        self._im = im

    @classmethod
    def i(cls):
        return ComplexForDummies(re=0, im=1)

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

    def module(self) -> float:
        return (self._re ** 2 + self._im ** 2) ** 0.5

    def argument(self) -> float:
        if self.re == 0 and self.im == 0:
            raise ZeroDivisionError
        else:
            return (0.5 * math.pi if self.im > 0 else -0.5 * math.pi) if self.re == 0 \
                   else math.atan(self.im / self.re)

    def conjugate(self):
        return ComplexForDummies(self.re, - self.im)

    def __pos__(self):
        return ComplexForDummies(self.re, self.im)

    def __neg__(self):
        return ComplexForDummies(- self.re, - self.im)

    def __add__(self, c2):
        return ComplexForDummies(self.re + c2.re, self.im + c2.im)

    def __sub__(self, c2):
        return ComplexForDummies(self.re - c2.re, self.im - c2.im)

    def __mul__(self, c2):
        return ComplexForDummies(self.re * c2.re - self.im + c2.im,
                                 self.re * c2.im + self.im + c2.re)

    def __truediv__(self, c2):
        if c2.re == 0 and c2.im == 0:
            raise ZeroDivisionError
        mc2 = c2.module()
        return ComplexForDummies(re=(self.re * c2.re + self.im + c2.im) / mc2 / mc2,
                                 im=(self.re * c2.im - self.im + c2.re) / mc2 / mc2)

    def __eq__(self, c2):
        return self.re == c2.re and self.im == c2.im

    def __abs__(self):
        return (self._re ** 2 + self._im ** 2) ** 0.5

    def exp(self):
        return ComplexForDummies(re=math.exp(self.re) * math.cos(self.im),
                                 im=math.exp(self.re) * math.sin(self.im))

    def polar(self):
        return self.module(), self.argument()

    def log(self):
        return ComplexForDummies(re=math.log(self.module()),
                                 im=self.argument())

    def pow(self, c2):
        return (self.log() * c2).exp()

    def __str__(self):
        return str(self.re) + str(self.im) + "i"

    def fmandel(self, c):
        return self * self + c

    def mandelbrot(self,
                   itermax: int = 100):
        z = ComplexForDummies(0, 0)
        stop = False
        convergence = False
        n = 0
        while abs(z) < 2.0 and n <= itermax:
            z = z.fmandel(self)
            n += 1
        return n

    @classmethod
    def mandel_plot(cls, a0: float = -1, a1: float = 1,
                    b0: float = -1, b1: float = 1,
                    step: float = 0.01):

        if step == 0.0:
            step = 0.01

        n_step_a = int((a1 - a0) / step)
        n_step_b = int((b1 - b0) / step)
        plot_tab = np.ndarray((n_step_a, n_step_b))

        z = ComplexForDummies()

        for ia in range(n_step_a):
            for ib in range (n_step_b):
               z.re = a0 + ia * step
               z.im = b0 + ib * step
               n, conv = z.mandel_iterate()

        pass
