def adicionarProduto():
    for i in range(5):  
        listaDeProdutos = []
        codigo = int(input("Insira o código do produto: "))
        nome = input("Insira o nome do produto: ")
        preco = float(input("Insira o preço do produto: "))
        estoque = int(input("Insira o estoque do Item: "))
        if codigo < 1 :
            print("Código inválido")
        else:
            listaDeProdutos.append(codigo)
            listaDeProdutos.append(nome)
            listaDeProdutos.append(preco)
            listaDeProdutos.append(estoque)   
            print(listaDeProdutos)         
    return listaDeProdutos
    


print(adicionarProduto())
        

