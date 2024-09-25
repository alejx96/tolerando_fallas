import numpy as np
import matplotlib.pyplot as plt
#Ricardo Hernandez INTENTO Programa 1.

# Definir parámetros
A = 1        # Amplitud propuesta
f = 1        # Frecuencia propuesta en Hz
ω0 = 2 * np.pi * f  # Frecuencia angular ω0

# Definir el tiempo t para graficar (para varios ciclos)
t = np.linspace(0, 6 / f, 1000)  # 6 ciclos para h(t), por ejemplo

# Definir las funciones
def f_t(t, A, ω0):
    return A * np.sin(ω0 * t)

def g_t(t, A, ω0):
    return A * np.sin(2 * ω0 * t)

def h_t(t, A, ω0):
    return A * np.sin(3 * ω0 * t)

# 1. Graficar f(t), g(t), h(t) con diferentes ciclos
plt.figure(figsize=(10, 6))
plt.plot(t, f_t(t, A, ω0), label='f(t) = A sin(ω0t)', color='blue')
plt.plot(t, g_t(t, A, ω0), label='g(t) = A sin(2ω0t)', color='red')
plt.plot(t, h_t(t, A, ω0), label='h(t) = A sin(3ω0t)', color='green')
plt.axhline(0, color='black',linewidth=0.5)
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Señales f(t), g(t) y h(t)')
plt.legend()
plt.grid(True)
plt.show()

# 2. Graficar f(t) y su valor eficaz (RMS)
rms_value = A / np.sqrt(2)
plt.figure(figsize=(10, 6))
plt.plot(t, f_t(t, A, ω0), label='f(t) = A sin(ω0t)', color='blue')
plt.axhline(rms_value, color='orange', label='Valor eficaz (RMS)')
plt.axhline(-rms_value, color='orange')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('f(t) y valor eficaz')
plt.legend()
plt.grid(True)
plt.show()

# 3. Graficar |f(t)| (valor absoluto de f(t))
plt.figure(figsize=(10, 6))
plt.plot(t, np.abs(f_t(t, A, ω0)), label='|f(t)|', color='purple')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Valor absoluto de f(t)')
plt.legend()
plt.grid(True)
plt.show()

# 4. Graficar f(t)^2 (valor cuadrático)
plt.figure(figsize=(10, 6))
plt.plot(t, f_t(t, A, ω0)**2, label='f(t)^2', color='brown')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude^2')
plt.title('Valor cuadrático de f(t)')
plt.legend()
plt.grid(True)
plt.show()

# 5. Graficar f(t) en decibeles (dB)
epsilon = 1e-10  # Un valor pequeño para evitar log(0)
f_db = 20 * np.log10(np.maximum(np.abs(f_t(t, A, ω0)), epsilon))

plt.figure(figsize=(10, 6))
plt.plot(t, f_db, label='f(t) en dB', color='magenta')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude (dB)')
plt.title('f(t) en decibeles')
plt.legend()
plt.grid(True)
plt.show()
