print('Welcome to my computer quiz')
playing = input("Do you want to play ?")
score = 0

if playing != "yes":
    quit()

print("okay! lets play")

answer = input ("What does cpu stand for?")
if answer.lower() =="Central processing unit":
    print('Correct')
    score += 1

else:
    print("Incorrect")

print("you got " + str(score)  + " questions correct!")
