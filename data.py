dd = int(input("Insira o dia: "))
mm = int (input("Insira o mês:"))
aaaa = int(input("Insira o ano: "))

if dd == 0 or dd > 31 :
    print("Dia inválido.")
elif mm == 0 or mm > 12 :
    print("Mês inválido")
elif aaaa == 0 or aaaa > 2022 :
    print("Ano inválido.")
elif dd < 10 and mm < 10 :
    print(f"0{dd}/0{mm}/{aaaa}")
elif dd < 10 :
    print(f"0{dd}/{mm}/{aaaa}")
elif mm < 10 :
    print(f"{dd}/0{mm}/{aaaa}")

else : 
    print(f"{dd}/{mm}/{aaaa}")