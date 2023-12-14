import re

# Using readlines()
file1 = open('Day2/input.txt', 'r')
Lines = file1.readlines()

# what is the fewest number of
# cubes of each color that could have 
# been in the bag to make the game possible?

# Parsing Games
#format: "Game number: gamen; gamen+1; .."


PowerList = []
for entry in Lines:
    x = entry.split(":")
    gameNumber = re.findall(r'\d+',x[0])

    gameSetString = x[1]
    gameSet = gameSetString.split(";")
    
    red, green, blue = 0,0,0
    
    for game in gameSet:
        cubeAndCount = game.split(",")

        for color in cubeAndCount:
            Number = re.findall(r'\d+',color)
            if "blue" in color:
                # print("Blue: " + Number[0])
                if int(Number[0]) > blue:
                    blue = int(Number[0])
            elif "green" in color:
                if int(Number[0]) > green:
                    green = int(Number[0])
            elif "red" in color:
                if int(Number[0]) > red:
                    red = int(Number[0])
            else:
                print ("NON MATCHING COLOUR FOUND, GAME RULES BROKEN, EXITING")
                exit()         

    PowerList.append(red*green*blue)

print("Final Answer: " + str(sum(PowerList)))

                