numero = int(input("insira um número menor que 1000: "))

if numero > 1000 :
	print("Insira um numero até 1000")
else: 
	centena = numero//100
	centenax100 = centena *100
	dezena = (numero - centenax100) //10
	dezenax10 = dezena * 10
	unidade = (numero - centenax100 - dezenax10)

if centena > 1 :
	strcentena = "centenas"
else : 
 	strcentena = "centena"

if dezena > 1 : 
	strdezena = "dezenas"
else : 
	strdezena = "dezena"

if unidade > 1 :
	strunidade = "unidades"
else:
	strunidade = "unidade"

print(f" A quantidade de {strcentena} , {centena}, a quantidade de {strdezena} , {dezena} e a quantidade de {strunidade} , {unidade}.")