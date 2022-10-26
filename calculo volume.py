import math

def calculovolume(raio, altura):
    volume = math.pi * (raio**2) * altura
    return volume

raio = int(input('digite o raio'))
altura = int(input('digite a altura'))
volume = calculovolume(raio, altura)

print(volume)

    