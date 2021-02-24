import time
import keyboard
import enquiries

print("You open your eyes")

time.sleep(3)

print( "A powerful ray of light hits your eyes and you see a figure of a man standing above you")

time.sleep(2)

print("Stranger: H&%$y, w^34ke *$#p")

time.sleep(2)

print("His words echo in your head as you try to gain conciousness")

time.sleep(3)

print("Stranger: Hey, hey, please, wake up")

time.sleep(3)

print("You can finally understand his words")

time.sleep(2)

print("You open your eyes wide")

time.sleep(2)

print("Stranger: Thanks God you are alive!")

userName = input('What is your name? ')

time.sleep(1)

print('Oh,', userName, ", I am so glad I found you!")

time.sleep(2)

dial1 = ["Where am I?..", "Who are you?", "*Stay silent*"]
choice = enquiries.choose("Choose: ", dial1)
print(choice)
if (choice == "Where am I?.."):
    print("Stanger: At my place")
    time.sleep(2)
    print("Clark: By the way, my name is Clark")
elif (choice == "Who are you?"):
    print("Clark: My name is Clark, I work around here")
elif (choice == "*Stay silent*"):
    print("*The stranger stares at you with his curious eyes*")
    time.sleep(2)
    print("Clark: Well, my name is Clark by the way")

time.sleep(2)

print("Clark: How did you get yourself so deep in the woods?")

time.sleep(2)

print("*You try to stand up but fail and fall on the ground*")

time.sleep(2)

print("Wow,", userName, ", please be careful, you might be weak now")

time.sleep(2)

print("*He gentely puts you on the bed you fell from and walks away*")

time.sleep(4)

print("Clark: Let me bring some medication for you")

time.sleep(2)

print("While he is away, you try to remember what exactly happened to you")

time.sleep(2)

print("You understand that the only thing you remember is your name")

time.sleep(2)

print("*Clark comes back to you with a glass of water and some medication*")

time.sleep(2)

print("Clark: Hey, are you fine? Can you speak?")

dial2 = ["Thank you, Clark", "Where did you find me?", "*Take the medication*"]
choice = enquiries.choose("Choose: ", dial2)
print(choice)
if (choice == "Thank you, Clark"):
    print("*Clark smiles at you showing his pure white teeth*")
    time.sleep(2)
    print("Clark: That's what everyone should do, I just helped you")
elif (choice == "Where did you find me?"):
    print("Clark: Very far from a place I have ever seen a man")
    time.sleep(3)
    print("Clark: You were just laying and I thought you were... well... dead")
    time.sleep(3)
    print("Clark: But surprisingly I understood that you are in fact alive and brought you to my place")
elif (choice == "Take the medication*"):
    print("*You take the medication and the glass of water Clark brought*")
    
time.sleep(3)    

print("*You hear a knock on the door*")

time.sleep(2)

print("*Clark walks away from you to open the door*")

time.sleep(2)

print("*You hear Clark and two other men talking*")

time.sleep(2)

print("*Suddenly, they stop talking and you hear sounds of footsteps*")

time.sleep(2)

print("*Naturally, you are very scared*")

time.sleep(2)

print("*Two men in police uniform walk into the room where you are*")

time.sleep(3)

print("Officer 1: Hello, Mr?..")

dial3 = ["*Say your Surname*", "What do you want?", "Stay silent"]
choice = enquiries.choose("Choose: ", dial3)
print(choice)
if (choice == "*Say your Surname*"):
    userSurname = input("*Enter a Surname*: ")
    time.sleep(2)
    print("Off. Williams: Well, mr.", userSurname, ", I am Officer Williams")
    time.sleep(2)
    print("*WIlliams looks at his partner*")
    time.sleep(2) 
    print("Off. Williams: This is officer Murphy")
