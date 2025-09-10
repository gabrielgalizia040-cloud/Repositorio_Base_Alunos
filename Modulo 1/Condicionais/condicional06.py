# Crie um codigo python que peca o valor da conta. se for maior que R$100,00,
# adicione uma gorjeta de 10% e exiba o total a pagar.
# Caso contrario, adicione uma gorjeta de 5%.

# etapas para resolucao
# 1) solicitar o valor da conta para o usuario
# 2) se a conta for maior que 100 adicionar 10% de gorjeta e apresentar o total a pagar
# 3) se a conta for maior que 100 aicionar 5% de gorjeta e apresentar o total a pagar 

 
conta = float(input("digitre o valor da conta R$: "))
if conta >= 100:
    # contra_final=conta +(conta *0.1)
    conta_final= conta*1.1
    print(f"obrigado por sua visita, sua conta e R$ {conta_final:.2f}")

else:
    conta_final = conta*0.05
    print(f"obrigado por sua visita, sua conta e R$ {conta_final:.2f}.")

 
