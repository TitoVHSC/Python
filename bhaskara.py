from multiprocessing.resource_sharer import stop
from re import X


import math
print("Bem vindo a calculadora de Bhaskara!")
a = float(input("Insira o valor do termo A: "))
if a == 0 :
    print("Não é uma equação de segundo grau. ")
else :
    b = float(input("Insira o valor do termo B: "))
    c = float(input("Insira o valor do termo C: "))

delta = (b*b) - (4 * a * c) 
x1 = (-b + delta ** (1 / 2)) / (2 * a)
x2 = (-b - delta ** (1 / 2)) / (2 * a)
 

if delta < 0 :
    print("A equação não possui raizes reais")
elif delta == 0 and x1 == 0 :
    print(f"A raiz real de x2 é : {x2}.")
elif delta == 0 and x2 == 0 :
    print(f"A raiz real de x1 é : {x1}.")
else:
    print(f"As raízes da equação são x1: {x1:.2f} e x2: {x2:.2f}.") 