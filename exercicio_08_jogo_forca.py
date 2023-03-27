"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra = 'manjericão'

letras_adivinhadas = ''

tentativas = 0

while True:
      
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        
        print('Digite apenas uma letra!')
        continue
    
    if letra in letras_adivinhadas:
        
        print('Você já digitou essa letra!')
        continue
    
    if letra in palavra:
        
        letras_adivinhadas += letra
        tentativas += 1
    
    else:
        
        tentativas += 1
    
    palavra_formada = ''    
    for letra in palavra:
        
        if letra in letras_adivinhadas:
            
            palavra_formada += letra
        
        else:
            
            palavra_formada += '*'
        
    print(palavra_formada)
    
    if palavra_formada == palavra:
        
        os.system('cls')
        print('Parabéns! Você acertou!!!')
        print(f'Você usou {tentativas} tentativas!')
        print(f'A palavra era {palavra_formada}')
        letras_adivinhadas = ''
        tentativas = 0