import random

number_to_guess = random.randint (1,20)  
attempt = 5

print("Welcome to the guessing game")
print("you have 5 attemp to guess the right number")

for attempt in range(1, attempt + 1):
    guess = int(input(f"Attempt {attempt}/{attempt} - Guess a number: "))

    if guess < number_to_guess :
        print("too low")   
    elif guess > number_to_guess : 
        print("too high")
    else :
        print(f"you got it, the number was {number_to_guess} in {attempt} attempts")
        break


if attempt < attempt :
    print(f"You have {attempt - attempt} attempts left.\n")
else : 
    print(f"Sorry you Have used all your attempts. the correct numebr was {number_to_guess}")



