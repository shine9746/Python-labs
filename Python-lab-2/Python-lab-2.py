#Fetch number from user and shows messages according to whether the number is even or odd

name = input("Enter user name")

randomnumber = int(input("Enter a number"))

operation = randomnumber % 2

if operation == 0:
    print("Hello"+ " " +name+",Congratulations you are a champion!!!") #Even number
else:
    print("Hello"+ " " + name+",Oops!!! Better luck next time.") #Odd number
