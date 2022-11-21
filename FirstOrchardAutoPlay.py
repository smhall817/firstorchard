# Import random package
import random

# Title
print("First Orchard\n")

# Establish variables
bird = 0
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
        print("The bird begins on space 0.")
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

    # Random result gets chosen from list
    die = [1, 2, 3, 4, 5, 6]
    faces = ["red apple", "yellow pear", "green apple", "blue plum", "bird", "basket"]
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
        print("The die result is " + faces[result-1] + "\n")

        # Increment/decrement variables, or alert user if no matching fruits...
        if result == 1:
            if red > 0:
                red -= 1
        elif result == 2:
            if yellow > 0:
                yellow -= 1
        elif result == 3:
            if green > 0:
                green -= 1
        elif result == 4:
            if blue > 0:
                blue -= 1
        elif result == 5:
            bird += 1
            print("The bird moves to the next space!")
            if bird >= 5:
                print("*********************************************\nThe bird reached the end of track! Game over!\n*********************************************\n")
                playing = False
        elif result == 6:
            choice = [red, yellow, green, blue]
            vals = [y for x,y in enumerate(choice)]
            m = max(vals)
            choice[vals.index(m)] = m - 1            
            red = choice[0]
            yellow = choice[1]
            green = choice[2]
            blue = choice[3]
            
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
