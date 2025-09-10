# crie um programa que:
# 1) peca ao usuario que difite um numero de 1 a 7 para indicar
# os dias da semana
# 2) use match case para exibir o nome correspondente ao numero:
# 1- domingo
# 2- segunda-feira
# 3- terca-feira
# 4- quarta-feira
# 5- quinta-feira
# 6- sexta-feira
# 7- sabado

print("dias da semana")
print(""" 1- dmingo
 2- segunda-feira
 3- terca-feira
 4- quarta-feira
 5- quinra-feira
 6- sexta-feira
 7- sabado""")
dia = int(input("digite um numero de 1 a 7: "))
match dia:
    case 1:
        print("e domingo.bom inicio de semana.")
    case 2:
        print("hoje e segunda-feira.boa semana.")
    case 3:
        print("hoje e terca-feira.")
    case 4:
        print("hoje e quarta-feira.")
    case 5:
        print("hoje e quinta-feira.")
    case 6:
        print("hoje e sexta-feira.")
    case 7:
        print("hoje e sabado.")
    case _:
        print("numero invalido. digite um numero de 1 a 7.")