nomeproduto1 = (input("Insira a marca do primeiro Produto: "))
nomeproduto2 = (input("Insira a marca do segundo Produto: "))
nomeproduto3 = (input("Insira a marca do terceiro Produto: "))

numero1 = (input("Insira o valor do primeiro produto: "))
numero2 = (input("Insira o valor do segundo produto: "))
numero3 = (input("Insira o valor do terceiro produto: "))

produto1 = "Marca: " + nomeproduto1 , " Valor: R$" + numero1
produto2 = "Marca: " + nomeproduto2 , " Valor: R$" + numero2
produto3 = "Marca: " + nomeproduto3 , " Valor: R$" + numero3


if   numero1 < numero2 and numero1 < numero3 :
    print(f"O produto mais barato é {produto1}")
elif numero2 < numero1 and numero2 < numero3 :
    print(f"O produto mais barato é {produto2}")
elif numero3 < numero1 and numero3 < numero3 : 
    print(f"O produto mais barato é {produto3}")