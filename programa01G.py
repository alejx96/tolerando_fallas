import matplotlib.pyplot as plt
import numpy as np

A = 2
f = 440
w0 = 2 * np.pi * f

# t = [10,20,30,40]
t = np.linspace(0,0.01,1000)
print('f(t)= Asen(w0t)','g(t)= Asen(2w0t)','h(t)= Asen(3w0t)',sep='\n')

Ft = []
Gt = []
Ht = []

for T in t:
    Ft.append(A * np.sin(w0 * T))
    Gt.append(A * np.sin(2 * w0 * T))
    Ht.append(A * np.sin(3 * w0 * T))

print(Ft)
print(Gt)
print(Ht)

plt.figure(figsize=(10,6))
plt.plot(t, A * np.sin(w0 * t), label='f(t)', color='blue')
plt.plot(t, A * np.sin(2 * w0 * t), label='g(t)', color='red')
plt.plot(t, A * np.sin(3 * w0 * t), label='h(t)', color='green')
# plt.plot(t, Ft, label='f(t)', color='blue')
# plt.plot(t, Gt, label='g(t)', color='red')
# plt.plot(t, Ht, label='h(t)', color='green')
plt.xlabel('Tiempo')
plt.ylabel('frecuencia')
plt.legend()
plt.show()
