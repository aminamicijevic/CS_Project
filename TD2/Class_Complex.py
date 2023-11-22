import math


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def mod(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)

    def arg(self):
        return math.atan2(self.imag, self.real)

    def conj(self):
        return Complex(self.real, -self.imag)

    def polar(self):
        modul = self.mod()
        argument = self.arg()
        return f"{modul} * exp({argument}i)"


z1 = Complex(3, 4)
print(z1.real)
# 3
print(z1.imag)
# 4
print(z1.mod())
# 5.0
print(z1.arg())
# 0.9272952180016122
print(z1.conj().imag)
# -4
print(z1.polar())
# '5.0* exp (0.92779 i) '
