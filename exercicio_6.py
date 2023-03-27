"""
Iterando strings com while
"""

nome = input('Digite o seu nome completo: ')

tamanho_nome = len(nome)

tamanho = 0

novo_nome = '*'

while tamanho < tamanho_nome:
    letra = nome[tamanho]
    print(letra)
    novo_nome += f'{letra}*'
    
    tamanho += 1

print(novo_nome)