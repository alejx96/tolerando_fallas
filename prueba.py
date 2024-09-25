import matplotlib.pyplot as plt

# Configurar el tamaño de grafico
plt.figure(figsize=(8,6))

hours = [2,3,4,5,6,7,8]
exam_scores_student_1 = [55, 60, 65, 70, 75, 80, 85]
exam_scores_student_2 = [50, 58, 63, 69, 74, 78, 83]

# Crear grafico de dispersión de los estudiantes
plt.scatter(hours, exam_scores_student_1, marker='o', color='green', label='Estudiante 1')
plt.scatter(hours, exam_scores_student_2, marker='s', color='red', label='Estudiante 2')

plt.title('Relacion entre horas estudiadas y el puntaje de 2 estudiantes')
plt.xlabel('Horas estudiadas')
plt.ylabel('Puntaje')

plt.show()