a = input("Enter a word : ")

if(a.casefold() == a[:: -1].casefold()):     #reversedvalue
    print("It is a palindrome")
else:
    print("It is not a palindrome")
