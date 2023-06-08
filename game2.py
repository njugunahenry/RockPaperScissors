import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0 :
        print("Please type a no.larger then 0")
        quit()
else:
        print("please type a no. next time")
        quit()


random_number = random.randint(0,top_of_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess:  ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("please type a no. next time")
        quit()
        continue

    if user_guess ==random_number:
        print("You go it")
        break
    else:
        if user_guess > random_number:
            print("you are above the no.")
        else:
            print('you are below the number.')


print("you got it in ",guesses,"guesses")

