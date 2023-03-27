""" Calculadora com while """

while True:
    
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o segundo número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        
        numeros_validos = True    

    except:
        
        numeros_validos = None

    if numeros_validos is None:
        
        print('Algum número digitado é inválido')
        
        continue
    
    operadores_permitidos = '+-*/'
    
    if operador not in operadores_permitidos:
        
        print('Operador inválido')
        
        continue
    
    if len(operador) > 1:
        
        print('Digite apenas um operador')
        
        continue
    
    if  operador == '+':
        
        print(f'Resultado:', round(num_1_float + num_2_float))
        
    elif  operador == '-':
        
        print(f'Resultado:', round(num_1_float - num_2_float))
        
    elif  operador == '*':
        
        print(f'Resultado:', round(num_1_float * num_2_float))
        
    elif  operador == '/':
        
        try:
            
            print(f'Resultado:', round(num_1_float / num_2_float))
        
        except ZeroDivisionError:
            
            print('Você não pode dividir um número por zero')
        
    else:
        
        print(f'Resultado:', ('Nunca deveria chegar aqui'))
    
    sair = input("Quer sair? [s]im: ").lower().startswith('s')
    
    if sair:
        
        break