# Import random package
import random

# Title
print("First Orchard\n")

# Establish variables
bird = 1
red = 4
yellow = 4
green = 4
blue = 4
roll_num = 1
playing = True

# Function for printing current game stats
def status():
    global roll_num
    if roll_num == 1:
        print("The bird begins on space 1.")
    else:
        print("The bird is currently on space " + str(bird) + " of 5\n")
    print("The remaining fruits are:")
    print(str(red) + " red apples")
    print(str(yellow) + " yellow pears")
    print(str(green) + " green apples")
    print(str(blue) + " blue plums\n")

# Print starting game state
status()

# Function for rolling die
def roll():

    # User presses enter to roll
    roll_die = input("Press enter to roll the die!")

    # Random result gets chosen from list
    die = ["basket", "bird", "red apple", "yellow pear", "green apple", "blue plum"]
    result = random.choice(die)

    # Function for updating game state based on roll
    def update():
        global red
        global yellow
        global green
        global blue
        global bird
        global roll_num
        global total_fruit
        global playing
        print("----------------------------\n")
        
        print("Roll #" + str(roll_num))
        print("The die result is " + result + "\n")

        # Increment/decrement variables, or alert user if no matching fruits...
        if result == "red apple":
            if red > 0:
                red -= 1
            else:
                print("No " + result + "s left. Nothing happens.")
        elif result == "yellow pear":
            if yellow > 0:
                yellow -= 1
            else:
                print("No " + result + "s left. Nothing happens.")            
        elif result == "green apple":
            if green > 0:
                green -= 1
            else:
                print("No " + result + "s left. Nothing happens.")
        elif result == "blue plum":
            if blue > 0:
                blue -= 1
            else:
                print("No " + result + "s left. Nothing happens.")

        # ... or else move the bird...
        elif result == "bird":
            bird += 1
            print("The bird moves to the next space.")
            if bird >= 5:
                print("The bird reached the fruit! Game over.")
                playing = False

        # ... or else let the user choose
        elif result == "basket":

            # Ask user for input
            while True:
                choice = input("Which fruit would you like to choose? Enter R for red apple, Y for yellow pear, G for green apple, or B for blue plum.\n")
                choice = choice.upper()

                # Validate input
                if choice not in ("R", "Y", "G", "B"):
                    print("Invalid input. Please try again.")
                    continue

                # Based on user input, make sure there are fruits remaining and then decrement
                else:
                    if choice == "R":
                        if red > 0:
                            red -=1
                        else:
                            print("No red apples left. Please pick another fruit.")
                            continue
                    if choice == "Y":
                        if yellow > 0:
                            yellow -=1
                        else:
                            print("No yellow pears left. Please pick another fruit.")
                            continue
                    if choice == "G":
                        if green > 0:
                            green -=1
                        else:
                            print("No green apples left. Please pick another fruit.")
                            continue
                    if choice == "B":
                        if blue > 0:
                            blue -=1
                        else:
                            print("No blue plums left. Please pick another fruit.")
                            continue
                    break

        # Increment roll number    
        roll_num += 1

        # Calculate total number of fruits remaining, and end game if 0
        total_fruit = (red + yellow + green + blue)
        if total_fruit == 0:
            print("********\nYOU WIN!\n********\n")
            playing = False

    # Run update and status functions
    update()
    status()
    return result

# As long as the game is in progress, continue prompting the user to roll
while playing == True:
    roll()
