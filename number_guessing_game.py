import random

top_of_range = input("enter a number: ")


if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("please enter a number greater than zero")
        quit()

else:
    print("enter a digit next time")  
    quit()      


random_number = random.randint(0,top_of_range)

guess_count = 0 



while True: 
    guess_count += 1
    guess = input("guess a number: ")


    if guess.isdigit():
        guess = int(guess)    
    else:
        print("enter a digit next time") 
        continue

    if guess == random_number:
        print("you got it!")
        break
    elif guess > top_of_range:
        print("you were above the number!")
    else:
        print("you got it wrong!")

print(f"you got it in {guess_count} guesses")
    