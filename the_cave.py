#all the import
from time import sleep

#all the def
def print_s(text):
	print(text)
	sleep(1)

def logo():
	print("==================")
	print("Project: The Cave")
	print("==================" + "\n") ; sleep(1)

def menu():
	print("1 > Start Game")
	print("2 > Quit Game") ; sleep(1)
	global menu_choice
	menu_choice  = input("What is your choice ? > ")
	menu_choices()

def menu_choices():
	while True:
		if menu_choice == "1":
			print("Good Luck...")
			countdown()
			break
		elif menu_choice == "2":
			break
		elif menu_choice != "1" and menu_choice != "2":
			print("Try Again")
			menu()
			break

def countdown():
	for i in reversed(range(5)):
		print(i+1) ; sleep(1)
	print("0") ; sleep (1)
	explore_cave()
	
def explore_cave():
    print_s("You find yourself standing at the entrance of a mysterious cave.")
    sleep(1)
    print_s("You enter the cave and come across a fork in the path.") ; sleep(1)
    print_s("Which path will you choose?")
    print_s("1. Take the left path")
    print_s("2. Take the right path")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        print_s("You follow the left path and encounter a rickety bridge.")
        print_s("What will you do?")
        print_s("1 - Cross the bridge")
        print_s("2 - Find another way")
        choice = input("Enter your choice (1 or 2) >  ")

        if choice == "1":
            print_s("You cautiously cross the bridge and continue on.")
            print_s("After a while, you reach a dead end.")
            print_s("You turn back and take the right path.")
            explore_cave()
        elif choice == "2":
            print_s("You decide to find another way.")
            print_s("You take the right path and continue exploring.")
            explore_cave()
        else:
            print_s("Invalid choice. Please try again.")
            explore_cave()

    elif choice == "2":
        print_s("You take the right path and find a dark tunnel.")
        print_s("What will you do?")
        print_s("1 - Use a flashlight to navigate through the tunnel")
        print_s("2 - Feel your way through the darkness")
        choice = input("Enter your choice (1 or 2) >  ")

        if choice == "1":
            print_s("You use your flashlight and carefully make your way through the tunnel.")
            print_s("Suddenly, you hear a loud noise and see a shadow approaching.")
            print_s("What will you do?")
            print_s("1 - Hide and wait")
            print_s("2 - Confront the shadow")
            choice = input("Enter your choice (1 or 2) >  ")

            if choice == "1":
                print_s("You hide and wait for the shadow to pass.")
                print_s("Once it's safe, you continue deeper into the cave.")
                explore_cave()
            elif choice == "2":
                print_s("You gather your courage and confront the shadow.")
                print_s("To your surprise, it turns out to be a friendly creature.")
                print_s("It leads you to a secret passage that leads to the treasure.")
                print_s("Congratulations! You found the hidden treasure!")
            else:
                print_s("Invalid choice. Please try again.")
                explore_cave()
        elif choice == "2":
            print_s("You decide to feel your way through the darkness.")
            print_s("Unfortunately, you lose your way and end up back at the entrance.")
            explore_cave()
        else:
            print_s("Invalid choice. Please try again.")
            explore_cave()

    else:
        print_s("Invalid choice. Please try again.")
        explore_cave()

#all the game
logo()
menu()