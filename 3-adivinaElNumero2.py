""" Adivina el Numero 2.

El usuario dará un numero y la computadora deberá adivinarlo.
"""
import random
import time
def IngresaNumero():
    numero_usuario = int(input("Escoge un numero: "))
    return numero_usuario

def adivinar_el_numero():
    x = IngresaNumero() # El numero que el usuario escogió = 60
    limiteInf = 0
    limiteSup = (x**2)//x
    intentos = 0
    while True:
        time.sleep(1)
        num = random.randint(limiteInf, x + limiteSup) # limite inf = 57 limite sup = 70  = 
        while limiteInf > num:
            limiteInf -= 1
        while limiteSup < num:
            limiteSup += 1
        if num < x:
            limiteInf = num
            print(f"El numero es mayor que {num}")
        elif num > x:
            limiteSup = num
            print(f"El numero es menor que {num}")
        else:
            print(f"El numero que escogiste es {num}\nSe logro en {intentos} intentos")
            break
            
        intentos += 1
if __name__ == '__main__':
    adivinar_el_numero()