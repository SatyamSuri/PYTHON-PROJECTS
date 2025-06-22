import random
target = random.randint(1,100)

while True:
    userChoice = int (input("Guess the target : "))
    if(userChoice == target):
        print("sucess : correct guess!!")
        break
    elif(userChoice < target):
        print("your number is too small. take a bigger number..")
    else:
        print("your number is too big. take a smaller number..")

print("_________GAME OVER_________")
