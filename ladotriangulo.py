lado1 = float(input("Insira o valor do primeiro lado do triângulo: "))
lado2 = float(input("Insira o segundo lado do triângulo: "))
lado3 = float(input("Insira o terceiro lado do triângulo: "))

if lado1  == lado2 and lado1 == lado3 : 
    print("Esse triângulo é Equilatero")
elif lado1 == lado2 and lado1 != lado3 or lado1 != lado2 and lado1 == lado3 : 
    print("Esse triângulo é Isósceles")
elif lado1 != lado2 and lado1 !=lado3 :
    print("É um triângulo Escaleno")
else: 
    print("Não é um triângulo.")