while True:
    
    number_1 = input('First number: ')
    number_2 = input('Second number: ')
    operator = input('Operator (+-/*): ')
    
    valid_number = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        
        num_1_float = float(number_1)
        num_2_float = float(number_2)
        
        valid_number = True    

    except:
        
        valid_number = None

    if valid_number is None:
        
        print('Invalid number')
        
        continue
    
    operadores_permitidos = '+-*/'
    
    if operator not in operadores_permitidos:
        
        print('Invalid operator')
        
        continue
    
    if len(operator) > 1:
        
        print('Type only one operator')
        
        continue
    
    if  operator == '+':
        
        print(f'Result:', round(num_1_float + num_2_float))
        
    elif  operator == '-':
        
        print(f'Result:', round(num_1_float - num_2_float))
        
    elif  operator == '*':
        
        print(f'Result:', round(num_1_float * num_2_float))
        
    elif  operator == '/':
        
        try:
            
            print(f'Result:', round(num_1_float / num_2_float))
        
        except ZeroDivisionError:
            
            print('You cannot divide by 0')
        
    else:
        
        print(f'Result:', ('Should never run this part'))
    
    quit = input("Quit? [y]es: ").lower().startswith('y')
    
    if quit:
        
        break