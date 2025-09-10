# 1) Receber o **peso** e a **altura** do usuário, calcular o **IMC** e exibir:
# 2) O valor calculado
# 3) Uma mensagem de orientação baseada no resultado
# 4) O usuário informa o **peso (kg)** e a **altura (m)**.
# 5)  O programa calcula o IMC:
# 6)  IMC = peso / (altura ** 2)
# 7)  O IMC é exibido junto com uma mensagem personalizada:
# 8) IMC ≥ 30.0 → `Cuidado com a Saúde`
# 9) IMC < 30.0 → `Tudo ok`

nome = (input("digite o seu nome"))
peso = float(input("digite o primeiro numero"))
altura = float(input("digite o segundo numero"))
IMC = float(input("calcular peso + altura"))
IMC = peso / (altura ** 2)
if nome:
    print(f"digite o nome {nome}: ")
elif peso:
    print(f"digite o seu peso {peso}: ")
elif altura:
    print(f"digite a sua altura {altura}: ")
elif IMC:
    print(f"calcular peso {peso} + altura {altura}")
elif IMC:
    print(f"mandar a mensagem cuidado com a saude quando for >= 30.0 ")
else:IMC
print(f"mandar a mensagem tudo okse estiver <= 30.0 ")