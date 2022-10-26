hora = float(input("digite a quantidade de horas trabalhadas por mês: "))
salariohora = float(input('digite o valor da sua remuneração por hora '))
 
salariobruto = hora*salariohora
taxair900 = salariobruto*0
taxair1500 = salariobruto*0.05
taxair2500 = salariobruto* 0.10
taxair2501 = salariobruto* 0.20
taxainss = salariobruto*0.1
fgts = salariobruto*0.11
taxasindicato = salariobruto*0.03

descontotal900 = taxair900 + taxainss + taxasindicato + fgts
descontotal1500 = taxair1500 + taxainss + taxasindicato + fgts
descontotal2500 = taxair2500 + taxainss + taxasindicato + fgts
descontotal2501 = taxair2501 + taxainss + taxasindicato + fgts
salarioliquido900 = salariobruto - descontotal900
salarioliquido1500 = salariobruto - descontotal1500
salarioliquido2500 = salariobruto - descontotal2500
salarioliquido2501 = salariobruto - descontotal2501

if salariobruto <= 900 :
    print(f'salário bruto : {salariohora} * {hora} : {salariobruto}')
    print(f'(-) IR (5%) : {taxair900}')
    print(f'(-) INSS (10%) : {taxainss}')
    print(f'(-) Sindicato (3%) :  {taxasindicato}')
    print(f'FGTS (11%) : {fgts}')
    print(f' Total descontos : {descontotal900}')
    print(f'Salário liquido : {salarioliquido900}')
else: 
    print("invalido")


