from random import randint

name = input('what is your name? ')
print(f'well {name} lets play a number guessing game shall we ')

number = randint(1,20)

print('i am thinking of a number between 1 to 20 guess the number in 5 guesses ')

for i in range(1,6):
    guess = int(input('what is your guess: '))
    if guess < number:
        print('your guess is too low')
    elif guess > number:
        print('your guess is too high')
    elif guess == number:
        print(f'congrats {name} you beat me the number i was thinking of was {str(number)}')
    else:
        break

print(f'your five tries is over the number i was thinking was {str(number)}')