#Decision Tree Program: Game Purchase Decision Tree
#Team Members: Griffin, Tristan, Cooper
#Date: 11/17/2025
#Description: This tree decides if or if not a certain game is worth being purchased.


#prompts the user with a yes or no question
d1 = str(input("Is the game above $30?(y/n):")).lower()
#Don't buy a game for over $30
if d1 == "y":
    print("Don't Buy")
elif d1 == "n":
    d2 = str(input("Is the game AAA?(y/n):")).lower()
#If the game is $30, and the game is Triple A, pirate it
    if d2 == "y":
        print("Pirate it")
    elif d2 == "n":
        d3 = str(input("Do you have any money?(y/n): ")).lower()
#If money is avilable or if the game isn't made my toby fox, wishlist
        if d3 == "n":
            print("Wishlist it and wait for sale")
#If money is avilable and is made by toby fox, buy
        elif d3 == "y":
            d4 = str(input("Is it made by Toby Fox?(y/n): ")).lower()
            if d4 == "n":
                print("Wishlist it and wait for sale")
            elif d4 == "y":
                print("Buy")
