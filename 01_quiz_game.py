print("Welcome to Computer quiz!")

playing = input("Do you want to play game? ")


if playing.lower() != "yes":
    quit()

print("Okay! Let's play :) ")
score = 0

answer = input("What does CPU stands for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What does GPU stands for? ")

if answer.lower() == "graphic processing unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What does RAM stands for? ")

if answer.lower() == "random access memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


answer = input("What does ROM stands for? ")

if answer.lower() == "read only memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")


# print("You got " , " correct questions! ")
print("You got " + str(score) + " correct questions! ")
print("You got " + str((score/4)*100) + "%.")