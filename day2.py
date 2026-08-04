import random
while True:
    choice = input('do you want play a (y/n): ').lower()
    if choice == "y":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print(f'{dice1, dice2}')
    elif choicey == 'n':
        print("thanks for playing the game")