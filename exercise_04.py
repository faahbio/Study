name = input('Tell me your name: ')
age = input('Tell me your age: ')


if name and age:
    
    print(f'Your name is {name}')
    
    print(f'Your inverted name is {name[::-1]}')
    
    if ' ' in name:
    
        print(f'Your name has spaces')
    
    else:
        
        print(f"Your name doesn't have spaces")
        
    print(f'Your name has {len(name)} letters')

    print(f'The first letter of your name is {name[0]}')
        
    print(f'The last letter of your name is {name[- 1]}')
    
else:
    
    print("Sorry, you've left something blank")