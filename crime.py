print("Responda as perguntas apenas com sim ou não.")

a = str(input("Telefonou para a vítima?: "))
b = str(input("Esteve no local do crime?: "))
c = str(input("Mora perto da vítima?: "))
d = str(input("Devia para a vítima?"))
e = str(input("Já trabalhou para a vítima?: "))

if a and b and c and d and e == "sim" :
    print("Culpado.")
