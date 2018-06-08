from random import randint
randomInt = randint(0,9)
print(randomInt)
while True:
    userInput = int(input("\n Guess the digit: "))
    if randomInt==userInput:
        print("Your answer is PERFECT!!(Congratulations!!)")
        break
    elif randomInt > userInput:
        print("Your answer is low than required")
    else:
        print ("You answer is high than required")