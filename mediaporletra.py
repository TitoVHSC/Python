nota1 = float(input('insira a primeira nota '))
nota2 = float(input('insira a segunda nota '))
media = (nota1 + nota2)/2

if media >= 9 :
    print("Aluno Aprovado com nota A")
elif media >= 7.5 < 9 :
    print("Aluno Aprovado com nota B")
elif media >= 6 < 7.5 : 
    print("Aprovado com Nota C")
elif media >= 4 < 6 :
    print("Reprovado com nota D")
else :
    print("Aluno Reprovado com média E")
