import numpy as np
import pandas as pd
import soundfile

class saludo():
    def __init__(self, nombre):
        self.nombre = nombre
        
    def mensaje(self):
        print("Bienvenido ", self.nombre)

mensaje = saludo("Me tire el archivo")