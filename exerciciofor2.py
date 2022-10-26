qntquartos = int(input("Insira a quantidade de quartos:"))
valorSimples = float(input("Insira a o valor do quarto simples: "))
valorDuplo = float(input("Insinra o valor do quarto duplo: "))
valorAlarme = float(input("Insira o valor da taxa de alarme: "))

for i in range(qntquartos) :
    tipoQuarto = int(input("Insira o tipo do quarto (1 - Simples , 2 - Duplo"))
    alarmeQuarto = int(input("Insira a quantidade de serviços de alarme solicitado: "))
    Consumo = float(input("Insira o valor de consumo no quarto"))
    if tipoQuarto == 1:
        valorQuarto = simples 
    elif tipoQuarto == 2:
        valorQuarto = duplo
    else :
        print("Valor de quarto inválido.")

