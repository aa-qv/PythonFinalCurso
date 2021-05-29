
def triangulo(n):
    for i in range(1, n+1):
        print(' '*(n-i) + '#'*i)
        
while True:

    n=int(input('Ingrese un número: '))
    
    if n>0 and n<9:
        triangulo(n)
        break
    else:
        print('Ingrese otro número: ')
