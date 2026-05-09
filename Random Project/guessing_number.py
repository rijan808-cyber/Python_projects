from random import randint
random_number=randint(1,100)
attempt=0
while True:
    guess=int(input('Enter any number to guess: '))
    if guess==random_number:
        attempt+=1
        print('--'*30)
        print('Congratulations you have guessed the number successfully')
        break
    elif guess<random_number:
        print('Sorry!! Try again')
        print('Random number is greater than you have guessed...')
        attempt+=1
    else:
        print('Sorry!! Try again')
        print('Random number is less than you have guessed...')
        attempt+=1

print(f'Total attempt taken: {attempt}')

