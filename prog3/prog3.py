import matplotlib.pyplot as plt
import numpy as np

w0 = 2 * np.pi

tG = np.linspace(0, 2 * (2 * np.pi) / w0, 1000)

fG = 6 + 5 * np.sin(w0 * tG)

#Grafique dos periodos de la senal g(t)
plt.figure(figsize=(10,6))
plt.title('Grafica de dos periodos de la senal g(t)')
plt.plot(tG, fG, label='g(t) = 6 + 5sen(ω0t)', color='blue')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()