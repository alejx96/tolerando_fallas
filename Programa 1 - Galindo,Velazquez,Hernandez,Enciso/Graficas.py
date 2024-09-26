import numpy as np
import matplotlib.pyplot as plt

# Definición de parámetros
A = 1  # Amplitud
omega0 = 2 * np.pi  # Frecuencia angular base
t_f = np.linspace(0, 2 * 2 * np.pi / omega0, 1000)  # Tiempo para dos periodos de f(t)
t_g = np.linspace(0, 4 * 2 * np.pi / (2 * omega0), 1000)  # Tiempo para cuatro periodos de g(t)
t_h = np.linspace(0, 6 * 2 * np.pi / (3 * omega0), 1000)  # Tiempo para seis periodos de h(t)

# Definición de las funciones
f_t = A * np.sin(omega0 * t_f)
g_t = A * np.sin(2 * omega0 * t_g)
h_t = A * np.sin(3 * omega0 * t_h)

# Gráfica de dos periodos de f(t), cuatro de g(t) y seis de h(t)
plt.figure(figsize=(10, 6))
plt.plot(t_f, f_t, label='f(t) = A sin(ω0t)', color='blue')
plt.plot(t_g, g_t, label='g(t) = A sin(2ω0t)', color='green')
plt.plot(t_h, h_t, label='h(t) = A sin(3ω0t)', color='red')

# Configuración de la gráfica
plt.title('Señales f(t), g(t), h(t) en varios periodos')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()

# Cálculo del valor eficaz (RMS) de f(t)
rms_f = np.sqrt(np.mean(f_t**2))  # Valor eficaz de f(t)

# Gráfica de un periodo de f(t) junto con su valor eficaz
t_f_1 = np.linspace(0, 2 * np.pi / omega0, 1000)  # Un periodo de f(t)
f_t_1 = A * np.sin(omega0 * t_f_1)

plt.figure(figsize=(10, 6))
plt.plot(t_f_1, f_t_1, label='f(t) = A sin(ω0t)', color='blue')
plt.axhline(y=rms_f, color='orange', linestyle='--', label=f'Valor eficaz (RMS) = {rms_f:.2f}')

# Configuración de la gráfica
plt.title('Señal f(t) y su valor eficaz')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()

# Gráfica del valor absoluto de f(t) para dos periodos
t_f_2 = np.linspace(0, 2 * 2 * np.pi / omega0, 1000)  # Dos periodos de f(t)
f_abs_t = np.abs(A * np.sin(omega0 * t_f_2))

plt.figure(figsize=(10, 6))
plt.plot(t_f_2, f_abs_t, label='|f(t)|', color='purple')

# Configuración de la gráfica
plt.title('Valor absoluto de f(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()

# Gráfica del valor cuadrático de f(t) para dos periodos
f_squared_t = (A * np.sin(omega0 * t_f_2))**2

plt.figure(figsize=(10, 6))
plt.plot(t_f_2, f_squared_t, label='$f^2(t)$', color='brown')

# Configuración de la gráfica
plt.title('Valor cuadrático de f(t)')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.show()

# Gráfica de f(t) en decibeles
f_db_t = 20 * np.log10(np.abs(f_t_1))

plt.figure(figsize=(10, 6))
plt.plot(t_f_1, f_db_t, label='f(t) en dB', color='magenta')

# Configuración de la gráfica
plt.title('Señal f(t) en decibeles')
plt.xlabel('Tiempo (t)')
plt.ylabel('Amplitud (dB)')
plt.grid(True)
plt.legend()
plt.show()
