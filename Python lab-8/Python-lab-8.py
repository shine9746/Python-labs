import random

userinput = int(input("Enter a number : "))
      
userguess= random.randint(1, 9)


while userguess != userinput and userguess != "break":
    userguess = int(input("Enter a guess between 1 to 9 : "))

    if userguess == "break":
        break


    if userguess < userinput:
        print("Too low...")
    elif userguess > userinput:
        print("Too high...")
    else:
        print("Exactly right!!!")
      
