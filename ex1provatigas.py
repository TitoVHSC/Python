numeros = []
for numero in range(10):
   numero =  int(input("Insira um número: "))
if numero > 0 :
    if numero >= 50 and  numero <= 100:
        numeros.append(numero)
    elif numero < 50:
        print(f"{numero} é menor que 50")
    elif numero > 100:
            print(f"{numero} é maior que 100")
    else:
        print(f"{numero} é negativo")


media = sum(numeros)
tamanho = len(numeros)
print(media / tamanho)
print(numero)
print(numeros)