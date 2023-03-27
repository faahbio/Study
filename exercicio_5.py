"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro: ')

if numero.isdigit:
    
    if (int(numero) % 2) is 0:
        
        print(f'{numero} é um número par')
    
    else:
        
        print(f'{numero} é um número impar')
    
else:
    
    print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são? Digite apenas a hora, sem minutos (24h): ')


try: 
    
    if hora.isdigit:
    
        if int(hora) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 24]:
            
            print('Bom dia')
        
        elif int(hora) in [12, 13, 14, 15, 16, 17]:
            
            print('Boa tarde')
        
        elif int(hora) in [18, 19, 20, 21, 22, 23]:
            
            print('Boa noite')
            
        else:
            
            print('O horário informado extrapola as 24h do dia')
            print('Informe um número inteiro entre 0 e 24')

except ValueError:
    
    print('Informe um número inteiro entre 0 e 24')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu primeiro nome: ')

try:
        
    if len(nome) <= 4:
            
        print('Seu nome é curto')
        
    elif len(nome) > 4 and len(nome) < 7:
            
        print('Seu nome é normal')
            
    else:
            
        print('Seu nome é muito grande')
            
except Exception:
        
    print('Erro')