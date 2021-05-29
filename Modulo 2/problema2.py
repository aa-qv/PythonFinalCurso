import sys

ABECEDARIO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

if __name__=='__main__':

    plaintext="HELLO"

    a=int(input('Valor de desplazamiento: '))

    ciphertext=""
    for l in plaintext:
        if l.upper() in ABECEDARIO:
            ciphertext += ABECEDARIO[(ABECEDARIO.index(l)+a%(len(ABECEDARIO)))]
        else:
            ciphertext += l

    print(f'El texto cifrado es: {ciphertext}')