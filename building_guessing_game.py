secret_number = 1
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess a number between 1 and 10: '))
    guess_count += 1
    if guess == secret_number:
        print(f'Congratulations, you guessed the number {secret_number}!')
        break
        #break dipakai untuk memutuskan logika loop
    else:
        print('Sorry, try again')
