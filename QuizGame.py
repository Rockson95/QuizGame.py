print("Welcome to Rockson's Computer quiz")

playing = input("Do you want to play Rockson's Computer game?. yes/no ")

if playing.lower()!= "yes":
    quit()
print("Sure let's play the game :) ")
score = 0

question = input("What does CPU stand for? ")
if question.lower() == "central processing unit":
    print("Your answer is correct")
    score +=1
else:
 print('Your answer is incorrect')

 question = input("What does IP stand for? ")
if question.lower() == "internet protocol":
        print("Your answer is correct")
        score += 1
else:
        print('Your answer is incorrect')

print("You got "+  str((score/2)*100) +"%")


