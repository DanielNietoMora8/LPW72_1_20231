import time
import librosa
from librosa import display
import matplotlib.pyplot as plt

#Ejericicio 3
class Fibo:
    def __init__(self, num):
        self.num = num
        self.aux1 = 0
        self.aux2 = 1
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.contador >= self.num:
            raise StopIteration
        resultado = self.aux1
        self.aux1, self.aux2 =self.aux2, self.aux2 + self.aux1
        
        self.contador += 1
        return resultado

n = 15  
secuencia = Fibo(n)
for i in range(n):
    print(next(secuencia))
    time.sleep(5)


# Ejercicio 4
class Analizar:
    def __init__(self, audio):
        self.audio = audio

    def plot_audio_signal(self, single_channel=True):
        # Cargar el archivo de audio
        y, sr = librosa.load(self.audio, duration=30)
        
        # graficar la señal de audio
        plt.figure(figsize=(12, 6))
        if single_channel:
            librosa.display.waveshow(y, sr=sr)
        else:
            plt.subplot(2, 1, 1)
            librosa.display.waveshow(y[:len(y)//2], sr=sr)
            plt.subplot(2, 1, 2)
            librosa.display.waveshow(y[len(y)//2:], sr=sr)
        plt.title("Audio Signal")
        plt.show()

    def plot_spectrogram(self, grayscale=False, fmin=None, fmax=None, output_name="espectrograma_default.png"):
            # Cargar el archivo de audio
        y, sr = librosa.load(self.audio_file, duration=30)

        D = librosa.amplitude_to_db(librosa.stft(y), ref=np.max)
        
        cmap = "gray" if grayscale else "viridis"
        
        if fmin is not None and fmax is not None:
            librosa.display.specshow(D, sr=sr, cmap=cmap, x_axis='time', y_axis='log', vmin=fmin, vmax=fmax)
        else:
            librosa.display.specshow(D, sr=sr, cmap=cmap, x_axis='time', y_axis='log')
        
        plt.title("Spectrogram")
        plt.colorbar(format="%+2.0f dB")
        plt.savefig(output_name, bbox_inches="tight")
        plt.show()

audio = "/audio_parcial.mp3"

n = Analizar(audio)
n.plot_audio_signal(single_channel=True)
n.plot_spectrogram(grayscale=True, fmin=-80, fmax=80, output_name="mi_espectrograma.png")

#Ejercicio 5

import matplotlib.pyplot as plt

class Tienda:
    def __init__(self):
        self.inventario = {}
    
    def agregar_producto(self, producto, precio):
        if producto not in self.inventario:
            self.inventario[producto] = precio
        else:
            print(f"{producto} ya existe en el inventario.")

    def vender(self, producto):
        if producto in self.inventario:
            precio = self.inventario[producto]
            del self.inventario[producto]
            return precio
        else:
            print(f"{producto} no está en el inventario.")
            return None

    def grafica(self, datos, titulo, etiquetas):
        plt.figure(figsize=(8, 6))
        plt.bar(etiquetas, datos)
        plt.title(titulo)
        plt.xlabel("Productos")
        plt.ylabel("Precio")
        plt.show()

tienda = Tienda()

#agregar productos
tienda.agregar_producto("Primer Producto", 2000)
tienda.agregar_producto("Segundo Producto", 2500)
tienda.agregar_producto("Tercer Producto", 3000)
tienda.agregar_producto("Cuarto Producto", 3000)

#vender un producto
producto_vendido = "Segundo Producto"
precio_venta = tienda.vender(producto_vendido)
if precio_venta is not None:
    print(f"Se vendió {producto_vendido} por ${precio_venta}.")

#gráfica de precios
productos = list(tienda.inventario.keys())
precios = list(tienda.inventario.values())
tienda.grafica(precios, "Precios de Productos", productos)
