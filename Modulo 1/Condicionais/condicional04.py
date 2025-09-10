# crie um codigo em python que peca um numero ao usuario 
# e exiba "numero par" se ele for divisivel por 2.

# etapas de resolucao:

# 1) solicitar um numero ao usuario 
# 2) verificar se o numero e par ou impar
# 3) informar se o numero e par ou impar

numero = float(input("digite um numero:"))

if numero%2 == 0:
    print(f"o numero{numero} e par")
else:
    print(f"o numero{numero} e impar")
    
