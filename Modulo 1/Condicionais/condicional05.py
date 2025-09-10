# crie um codigo python que verifique se a senha digitada
# pelo usuario for "1234", exiba "acesso permitido".

# etapas para resolucao
# criar uma variavel e a atribuir a ela uma senha
# atraves de um input solicitar a senha ao usuario
# atraves da condicional checar se a senha e igual a senha armazenada
# liberar ou nao o acesso ao usuario

senha_usuario = "1234"

senha = input("digite sua senha: ")

if senha == senha_usuario:
    print("acesso liberado.")
else:
    print("acesso negado. tente novamente")
    