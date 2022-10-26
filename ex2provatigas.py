import sys


qntdQuartos = int(input('Digite a quantidade de quartos ocupados:\n'))
simples = float(input('Digite o valor da diária do quarto simples:\n'))
duplo = float(input('Digite o valor da diária do quarto duplo:\n'))
alarme = float(input('Digite o valor do serviço de alarme:\n'))
totalHotel = 0

for i in range(qntdQuartos):
    tipoQuarto = int(
        input('Digite o tipo do quarto(1 - simples, 2 - duplo):\n'))
    alarmeQuarto = int(
        input('Digite a quantidade de serviços de alarme solicitada:\n'))
    consumo = float(input('Digite o valor consumido no quarto:\n'))
    if (tipoQuarto == 1):
        valorQuarto = simples
    elif (tipoQuarto == 2):
        valorQuarto = duplo
    else:
        sys.exit()

    if (consumo > (valorQuarto * 0.50) and consumo <= (valorQuarto * 0.75)):
        desconto = 0.10
    elif (consumo > (valorQuarto * 0.75) and consumo <= (valorQuarto * 0.90)):
        desconto = 0.20
    elif (consumo > (valorQuarto * 0.90)):
        desconto = 0.25
    else:
        desconto = 0

    valorTotal = (valorQuarto + (alarmeQuarto * alarme) + consumo) - \
        ((valorQuarto + (alarmeQuarto * alarme) + consumo) * desconto)
    totalHotel = totalHotel + valorTotal
    print("Valor total do quarto: ", valorTotal)
    print("Valor bruto do quarto: ", valorQuarto +
          (alarmeQuarto * alarme) + consumo)
    print("Desconto do quarto: ",
          ((valorQuarto + (alarmeQuarto * alarme) + consumo) * desconto))

print("\n\n\nTotal de rendimento do hotel: ", totalHotel)