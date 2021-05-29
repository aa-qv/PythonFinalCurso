
import re

def contraseña(contraseña):
    if 0 < len(contraseña) < 26:
        if re.search('[a-z]', contraseña) or re.search('[A-Z]', contraseña):
            return True 
    
    return False
            

clave = input('Digite contraseña: ')

print(contraseña(clave))