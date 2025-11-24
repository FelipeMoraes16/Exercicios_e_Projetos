#Interando strings com while

nome = 'Felipe Moraes'
tamanho_nome = len(nome)
indice = 0
novo_nome = ''

while indice < tamanho_nome:
    caracter = nome[indice]
    novo_nome += f'*{caracter}'
    indice += 1

print(novo_nome)