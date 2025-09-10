# dada a lista original = [1,2,3,4], use .copy() para criar uma nova lista chamada copia.
# altere a copia (adicione o numero 99)
# e mostre as duas listas para verificar que sao independentes.

original = [1,2,3,4]
print(f"lista original: (original)")

copia = original.copy() # copiamos a lista
print(f"lista copia:{copia}") # apresentamos a lista

copia.append(99) # adicionamos um elemento na ultima posicao
print(f"lista copia apos o append:{copia}") # apresentamos 