import random 

number_range = random.randint(1, 20)

print(number_range)
print("Guess a number between 1 and 20: ")

guess = int(input())

while guess != number_range:
    if guess < number_range:
        print("Your guess is too low.")
    elif guess > number_range:
        print("Your guess is too high.")
    guess = int(input())

print("You guessed correctly!")
        

