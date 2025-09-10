# criar um codigo python que indique se a temperatura esta agradavel ou nao
# condicoes: 
# temperatura >= 30° informar que esta muito quente
# temperatura >= 20° informar que a temperatura esta agradavel
# temperatura >= 10° informar que esta frio
# temperatura abaixo de 10° informar que esta muito frio

# estapas para resolucao:
# 1) solicitar a temperatura para o usuario 
# 2) verificar a condicional
# 3) imprimir a resposta segundo a temperatura

temperatura =float(input("digite a temperatura do dia: "))

# if condicao:
 # bloco de codigo a ser executado
 #elif condicao:
  # bloco de nota a ser executado
# else:
  # bloco de notas a ser exewcutado

if temperatura >= 30:
    print(f"a temperatura do dia e {temperatura}°c e o dia esta muito quente.")
elif temperatura >=20:
    print(f"a temperatura do dia e {temperatura}°C e o dia esta agradavel.")
elif temperatura >=10:
    print(f"a temperatura do dia e {temperatura}°C e o dia esta frio.")
else:
    print(f"a temperatura do dia e {temperatura}°C e o dia esta muito frio.")
    
