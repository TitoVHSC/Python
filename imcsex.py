sexo = (str(input('informe seu sexo (feminino ou masculino) ')))
altura = (float(input('informe sua altura: ')))
if sexo == 'f':
    print("seu peso ideal é" , (62.1*altura-44.7))
elif sexo == 'm' :
    print("seu peso ideal é" , (72.7*altura)-58)
else:
    print('sexo inválido')
for i in range (1,50,2):
    print(i)