##-----------------------------------------------------##
#Problema 1
#-------------------------------------------------------
m = float(input('Ingrese cantidad de dinero depositado:' )) 
i = 0.04

for a in range(1,4):
    m = m * (1+i)
    print(f"El monto al final del año {a} será :{round(m,2)}")

#--------------------------------------------------------#
#Problema 2
#--------------------------------------------------------#
from math import sqrt
a= int(input('Ingrese un valor diferente a 0: '))
b= int(input('Ingrese el valor de b: '))
c= int(input('Ingrese el valor de c: '))
if a != 0:
    # discriminante (d)
    d= (b**2 - 4*a*c)
    
    if d<0: 
        print('Ecuación no presenta solución real')
    else: 
        x1= (-b+ sqrt(d))/(2*a)
        x2= (-b- sqrt(d))/(2*a)
        print(f'Los valores son {x1} y {x2}')
    
else:     
    print('El valor de a debe ser distinto a cero')