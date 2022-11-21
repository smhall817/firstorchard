def firstorchard():

    # Import random package
    import random

    # Establish variables
    bird = 0
    red = 4
    yellow = 4
    green = 4
    blue = 4
    roll_num = 1
    playing = True
    outcome = 0

    # Function for rolling die
    def roll():

        # Random result gets chosen from list
        die = [1, 2, 3, 4, 5, 6]
        result = random.choice(die)

        # Function for updating game state based on roll
        def update():
            nonlocal red
            nonlocal yellow
            nonlocal green
            nonlocal blue
            nonlocal bird
            nonlocal roll_num
            nonlocal playing
            nonlocal outcome
            total_fruit = 0

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
                if bird >= 5:
#                    print("*********************************************\nThe bird reached the end of track! Game over!\n*********************************************\n")
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
                outcome = 1
#                print("********\nYOU WIN!\n********\n")
                playing = False

        # Run update and status functions
        update()
        return result

    while playing == True:
        roll()
    if playing == False:
        return (outcome, roll_num)

#firstorchard()
