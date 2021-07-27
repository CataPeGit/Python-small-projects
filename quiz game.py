print("Welcome to the quiz!")

playing = input('Do you want to play? ')


if playing.lower() != "yes":
    quit()
else:
    print("YEE! Let's play!!!")

score = 0

answer = input("What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect :/")

answer = input("what does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect :/")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect :/")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect :/")

print("You got " + str(score) + " questions!")
print("That is " + str((score/4) * 100) + "%")
