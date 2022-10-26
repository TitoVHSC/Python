

def taxainss(inss):
    insstx = inss*(1/100)
    return insstx

def calsalariobruto(valoraula, qntaula):
    salariobruto = valoraula*qntaula
    return salariobruto

def porcentagem(insstx):
    percentinss = insstx*salariobruto
    return percentinss

def calsalarioliquido(salariobruto, percentinss):
    salarioliq = salariobruto - percentinss
    return salarioliq
    
valoraula = (int(input("Insira sua remuneração por aula dada: ")))
qntaula = (int(input("Insira a quantidade de aulas dadas este mês: ")))
inss = (int(input("Insira o valor de desconto do seu INSS:")))

insstx = taxainss(inss)
percentinss = porcentagem(insstx)
salariobruto = calsalariobruto(valoraula,qntaula)
salarioliq = calsalarioliquido(salariobruto,percentinss)




print(f"O seu salário bruto é de {salariobruto} reais e o líquido é de {salarioliq} reais ")