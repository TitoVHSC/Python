pesopeixe = (float(input('Insira o peso do peixe: ')))
valormulta = 4
excedente = pesopeixe - 50
multa = excedente*valormulta
if pesopeixe < 50 :
    print('Não há cobrança de multa')
else :
    print(f'O valor a ser aplicado de multa é de {multa} reais')

