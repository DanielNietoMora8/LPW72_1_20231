# -*- coding: utf-8 -*-
"""SebastianTangarife_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dxVEAoQFYROUMcX8lKzZpdbwje7ax_iB
"""

import time

class Fibonacci:
    def _init_(self, n):
        self.n = n
        self.a, self.b = 0, 1
        self.current = 0

    def _iter_(self):
        return self

    def _next_(self):
        if self.current >= self.n:
            raise StopIteration
        else:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current += 1
            return result

n = int(input("Ingrese el número final para calcular Fibonacci: "))

if n < 0:
    print("El número final debe ser mayor o igual a 0.")
else:
    fib = Fibonacci(n)
    for value in fib:
        print(value)
        time.sleep(5)