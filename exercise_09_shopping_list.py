import os
import time

shop_list = []

while True:
    
    command = input('[i]nsert, [d]elete, [l]ist, [e]xit: ').lower()

    if command == 'i':

        os.system('cls')
        insert = input('Item you want to add: ')
        shop_list.append(insert)
        os.system('cls')
        print(f'You inserted {insert} on the list')
        time.sleep(2)
        os.system('cls')

    elif command == 'd':

        os.system('cls')

        print(f'Index \t Item')

        for number, item in enumerate(shop_list):

            print(f'{number} \t {item}')

        delete = int(input('Index you want to delete: '))

        try:

            shop_list.pop(int(delete))
            # del shop_list[delete]

            os.system('cls')

            print('Item deleted')

            time.sleep(1)

        except:

            os.system('cls')
            print('Index not found')
            time.sleep(3)
            os.system('cls')

    elif command == 'l':

        if len(shop_list) == 0:

            os.system('cls')
            print('Nothing on the list, add items to your list first')
            time.sleep(3)
            os.system('cls')
            continue

        os.system('cls')

        print(f'Index \t Item')

        for number, item in enumerate(shop_list):

            print(f'{number} \t {item}')

    elif command == 'e':

        os.system('cls')

        print('Thanks for using the list')

        time.sleep(3)

        os.system('cls')

        quit()

    else:

        print('Type: i to insert, d to delete, l to list or e to exit')
