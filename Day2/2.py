import re


# Using readlines()
file1 = open('Day2/input.txt', 'r')
Lines = file1.readlines()

# Determine which games would have been possible if the bag had been loaded with 
# only 12 red cubes, 13 green cubes, and 14 blue cubes.
#  What is the sum of the IDs of those games?

# Parsing Games
#format: "Game number: gamen; gamen+1; .."

validationRed = 12
validationGreen = 13
validationBlue = 14

counterTwo = 0
matchingGameIds = []
for entry in Lines:
    x = entry.split(":")
    gameNumber = re.findall(r'\d+',x[0])

    gameSetString = x[1]
    gameSet = gameSetString.split(";")
    
    gameIds = []
    counter = 1;

    for game in gameSet:
        cubeAndCount = game.split(",")
        red, green, blue = 0,0,0
        print(cubeAndCount)        
        for color in cubeAndCount:
            Number = re.findall(r'\d+',color)
            if "blue" in color:
                # print("Blue: " + Number[0])
                blue += int(Number[0])
            elif "green" in color:
                # print("Green: " + Number[0])
                green += int(Number[0])
            elif "red" in color:
                # print("Red: " + Number[0])
                red += int(Number[0])
            else:
                print ("NON MATCHING COLOUR FOUND, GAME RULES BROKEN, EXITING")
                exit() 
        print("Count Total: Red: "+ str(red) + " Green: " + str(green) + " Blue: " + str(blue))          
        if (red <= validationRed and green <= validationGreen and blue <= validationBlue):
            gameIds.append(counter)
        counter += 1
    counterTwo +=1
         
    print ("Matching IDs: ")
    print(gameIds)
    print(len(gameSet))
    if len(gameIds) == len(gameSet):
        print("Game ID: " + str(counterTwo) + " Valid")
        matchingGameIds.append(counterTwo)
    else:
        print("Game ID: " +  str(counterTwo) + " InValid")
        
print(matchingGameIds)
print("Final Sum of Valid Game IDs: " + str(sum(matchingGameIds)))
                