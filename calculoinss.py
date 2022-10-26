hora = float(input("digite a quantidade de horas trabalhadas por mês: "))
salariohora = float(input('digite o valor da sua remuneração por hora '))
 
salariobruto = hora*salariohora
print(f'{salariobruto} reais é o valor da sua remuneração mensal.')

taxair = salariobruto*0.11
taxainss = salariobruto*0.08
taxasindicato = salariobruto*0.05

descontotal = taxair + taxainss + taxasindicato
salarioliquido = salariobruto - descontotal

print(f'O total de horas trabalhadas é de {hora} horas por mês e o sálario bruto mensal é de {salariobruto} reais e desconta um total de {descontotal} reais. Sendo {taxair} reais de taxa do Imposto de renda, {taxainss} reais do inss e {taxasindicato} reais de taxa do sindicato')