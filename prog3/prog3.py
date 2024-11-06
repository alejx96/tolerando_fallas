import matplotlib.pyplot as plt
import numpy as np

w0 = 2 * np.pi

tG = np.linspace(0, 2 * (2 * np.pi) / w0, 1000)

fG = 6 + 5 * np.sin(w0 * tG)

# generacion puntos de las graficas de ruido r0 y r1
fRuido = 20 * w0
dStand1 = 0.4
dStand2 = dStand1 / 2

np.random.seed(0)

r0T = np.clip(np.random.normal(0, dStand1, len(tG)) * np.sin(fRuido * tG), -0.4, 0.4)
r1T = np.clip(np.random.normal(0, dStand2, len(tG)) * np.sin(fRuido * tG), -0.4, 0.4)

#Combinacion de senales
gR0 = fG + r0T
gR1 = fG + r1T

#Grafique dos periodos de la senal g(t)
plt.figure(figsize=(14,8))
plt.title('Grafica de dos periodos de la senal g(t)')
plt.subplot(3, 1, 1)
plt.plot(tG, fG, label='g(t) = 6 + 5sen(ω0t)', color='blue')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 2)
plt.title("Senales de ruido gaussiano r0 y r1")
plt.plot(tG, r0T, label='r0(t)', color='green')
plt.plot(tG, r1T, label='r1(t)', color='yellow')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.subplot(3, 1, 3)
plt.title("g(t) + r0 y g(t) + r1")
plt.plot(tG, gR0, label='g(t) + r0(t)', color='red')
plt.plot(tG, gR1, label='g(t) + r1(t)', color='blue')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()

plt.show()