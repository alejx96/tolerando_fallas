import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# definicion de listas
paises = ['Estados Unidos','Espana','Mexico','Rusia','Japon']
ventas = [25,32,34,20,25]

fig, ax = plt.subplots()

ax.set_ylabel('Ventas')
ax.set_title('Cantidad de Ventas por Pais')

plt.bar(paises,ventas)
# plt.savefig('D:\\clases\\6to Semestre\Computación Tolerante a Fallos(Optativa)\\programas\\barras_simple.png')

plt.show()