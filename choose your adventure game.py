name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, you can go left or right. Wich way would you like to go? ").lower()

if answer == "left":
    
    answer = input("You come to a river, you can walk around it or swim around. Type walk to walk around or swim to swim across. ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator. ")
    elif answer == "walk":
        print("You walked for many miles and ran out of water so you lost. ")
    else:
        print('Not a valid option. You lose. ')
    
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, you can head back or cross. ").lower()
    if answer == "back":
        print("You lose by going back. ")
    elif answer == "cross":
        
        answer = input("You cross the bridge and find a stranger. You can avoid him or talk to him. ").lower()
        if answer == "avoid":
            print ("You got lost. You lose.")
        elif answer == "talk":
            print("The stranger helped you go back home. You won!")
        else:
            print('Not a valid option. You lose. ')
            
    else:
        print('Not a valid option. You lose. ')

else:
    print('Not a valid option. You lose. ')

print("Thanks for playing", name + "!")
