from random import randint
print('\t DICE SIMULATOR')
print('Starting...')
while True:
    roll = input('Do you want to roll (y/n): ')
    if roll.lower() == 'y':
        print(f'you rolled: {randint(1,6)}')
    else:
        break