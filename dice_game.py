import random
print('Welcome to the Dice Game!')
while True:
    choice = input('do you want play a (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1},{die2})")
    elif choice == 'n':
        print('thank you for playing')
        break
    else:
        print('please enter y or n')