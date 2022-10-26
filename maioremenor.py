numero1 = float(input("Insira o primeiro numero:"))
numero2 = float(input("Insira o segundo numero: "))
numero3 = float(input("Insira o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3 :
    print(f"O maior numero é {numero1}")
elif numero2 > numero1 and numero2 > numero3 :
    print(f"O maior numero é {numero2}")
elif numero3 > numero1 and numero3 > numero2 :
    print(f"O maior numero é {numero3}")
else :
    print("Numero inválido")

if   numero1 < numero2 and numero1 < numero3 :
    print(f"o menor numero é {numero1}")
elif numero2 < numero1 and numero2 < numero3 :
    print(f" O menor numero é {numero2}")
elif numero3 < numero1 and numero3 < numero2:
    print(f" O menor numero é {numero3}")