#----------------------------------------------------#
#Probblema 1
#----------------------------------------------------#
alumnos = {}
cantidad = int(input("Introduce la cantidad de alumnos que vamos a guradar:"))
for num in range(cantidad):
    alumno = input("Nombre del alumno:")
    while alumno in alumnos:
        print("Alumno ya existe.")
        alumno = input("Nombre del alumno:")
    notas=[]
    nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    while nota > 0:
        notas.append(nota)
        nota = int(input("Dame una nota del alumno (negativo para terminar):"))
    alumnos[alumno] = notas.copy()

for alumno, notas in alumnos.items():
    print("%s ha sacado de nota media %f" % (alumno,sum(notas)/len(notas)))

#----------------------------------------------------#
#Probblema 1
#----------------------------------------------------#
def fun(nota):
    if nota > 7:
        return "Promociona"
    else:
        if nota < 4:
            return "Aplazado"
        else:
            if 4 <= nota <= 7:
                return "Aprobado"

#----------------------------------------------------#
#Probblema 1
#----------------------------------------------------#
from __future__ import division
 
def status(nota):
    if nota >=0 and nota < 4: return -1
    elif nota >= 4 and nota <=7: return 0
    elif nota > 7 and nota <= 10: return 1
    else: return None
 