"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os
import time

lista = []

while True:
    comando = input('[i]nserir, [a]pagar, [l]istar, [s]air: ').lower()
    
    if comando == ('i' or 'inserir'):
        
        os.system('cls')
        inserir = input('Item que você deseja adicionar: ')
        lista.append(inserir)
        os.system('cls')
        print( f'Você inseriu {inserir} na lista')
        time.sleep(2)
        os.system('cls')
        
    
    elif comando == ('a' or 'apagar'):
        
        os.system('cls')
        
        print(f'Indice \t Item')
        
        for numero, item in enumerate(lista):
            
            print(f'{numero} \t {item}')
            
        apagar = input('Item que deseja apagar: ')
        
        try:
            
            lista.pop(int(apagar))
            
            os.system('cls')
                       
            print('Item apagado')
            
            time.sleep(1)
        
        except:
            
            os.system('cls')
            print('Indice selecionado não está na lista')
            time.sleep(3)
            os.system('cls')
            
        
    elif comando == ('l' or 'listar'):
        
        if len(lista) == 0:
        
            os.system('cls')
            print('Nada para listar, adicione itens na lista')
            time.sleep(3)
            os.system('cls')
            continue
        
        os.system('cls')
    
        print(f'Indice \t Item')
        
        for numero, item in enumerate(lista):
            
            print(f'{numero} \t {item}')
        
    elif comando == ('s' or 'sair'):

        os.system('cls')
        
        print('Obrigado por usar a lista')
        
        time.sleep(3)
        
        os.system('cls')
        
        quit()

    else:
        
        print('Digite: i para inserir, a para apagar, l para listar ou s para sair')