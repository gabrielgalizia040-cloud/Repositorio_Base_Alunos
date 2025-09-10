# peca ao usuario para digitar uma letra
# se for vogal, informe qual vogal
# se for consoante, verifique se e maiuscula ou minuscula

# solicitacao de entrada de dados do tipo string (texto)
letra = input("digite uma letra: ")

if letra.lower() in "aeiou": # .lower() transforma para minuscula
    print(f"vogal: {letra}")
else:
    if letra.isupper(): # isupper identifica se a letra esta em mais 
        print("consoante maiuscula: {letra}")
    else:
        print(f"consoante maiuscula:{letra}")