def calcularAzulejo():
    lado1 = float(input("Insira lado 1 em metros: "))
    lado2 = float(input("Insira lado 2 em metros: "))
    metrosCaixa = float(input("Insira a quantidade de metros quadrados cada caixa cobre: "))
    valorCaixa = float(input("Insira o valor da Caixa: "))
    area = lado1 * lado2
    if lado1 < 0 or lado2 < 0 :
        print("Insira um números positivos.")
    else:
        aplicacao = int(input("Digite 1 para Aplicação paralela ou 2 para Aplicação diagonal: "))
        if aplicacao == 1:
            metrosParalela = area/metrosCaixa
            paralelaFinal =metrosParalela*1.1
            if paralelaFinal // 1 == 0:
                print("Não usará azulejos")
            else:
                qntFinal = (paralelaFinal//1) + 1
                print(f"A quantidade de caixas que serão gastas para cobrir {area}m² é de {qntFinal} caixas, custando um valor de R${qntFinal*valorCaixa*metrosCaixa}")
        elif aplicacao == 2:
            metrosDiagonal = area/metrosCaixa 
            DiagonalFinal = metrosDiagonal*1.15
            if DiagonalFinal // 1 == 0:
                print("Não usará caixas.")
            else:
                qntFinal = (DiagonalFinal//1) + 1 
                print(f"A quantidade de caixas que serão gastas para cobrir {area}m² é de {qntFinal} caixas, custando um valor de R${qntFinal*valorCaixa*metrosCaixa}")
        else:
            print("erro.")
    
    
print (calcularAzulejo())

