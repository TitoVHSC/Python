print("Calculo de Salário")
valorsalario = float(input("Insira o Salário Atual: "))
reajustesalario1 = valorsalario + valorsalario*0.20
reajustesalario2 = valorsalario + valorsalario*0.15
reajustesalario3 = valorsalario + valorsalario*0.10
reajustesalario4 = valorsalario + valorsalario*0.05

if valorsalario <= 280 :
    print(f" O salario antes do reajuste era de {valorsalario} reais e recebeu um reajuste de {valorsalario*0.20} reais (20%), totalizando um salário de {reajustesalario1} reais.")
elif valorsalario > 280 and valorsalario < 700 :
    print(f" O salario antes do reajuste era de {valorsalario} reais e recebeu um reajuste de {valorsalario*0.15} reais (15%), totalizando um salário de {reajustesalario2} reais.")
elif valorsalario > 700 and valorsalario < 1500 :
    print(f" O salario antes do reajuste era de {valorsalario} reais e recebeu um reajuste de {valorsalario*0.1} reais (10%), totalizando um salário de {reajustesalario3} reais.")
elif valorsalario > 1500 :
    print(f" O salario antes do reajuste era de {valorsalario} reais e recebeu um reajuste de {valorsalario*0.05} reais (5%), totalizando um salário de {reajustesalario4} reais.")


