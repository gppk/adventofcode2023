import re



def getDigitPosInLine(line):
    digitList = []
    for idx, ch in enumerate(line):
        if ch.isnumeric():
            digitList.append(idx)
    return digitList

def getSymbolPosInLine(line):
    asciiPos = []
    for idx, ch in enumerate(line):
        if False == (ch.isnumeric()) and ch != "." and ch != "\n":
            asciiPos.append(idx)
    return asciiPos

def findDigitPosWithSymbols(digitPos, symbolPosPrev, symbolPosCur, symbolPosNext):

    if not digitPos:
        return # No part numbers on this line

    digitsPosWithSymbols = []
    for idx, pos in enumerate(digitPos):
        # create spectrum array
        spectrum = [pos-1, pos, pos+1]
        if any(x in spectrum for x in symbolPosPrev):
            # print("Symbol found in previous pos for digitpos: " + str(pos))
            digitsPosWithSymbols.append(pos)
        
        if any(x in spectrum for x in symbolPosCur):
            # print("Symbol found in cur pos for digitpos: " +  str(pos))
            digitsPosWithSymbols.append(pos)

        if any(x in spectrum for x in symbolPosNext):
            # print("Symbol found in next pos for digitpos: " +  str(pos))
            digitsPosWithSymbols.append(pos)

    return digitsPosWithSymbols

partNumbers = []

def main(lines):    

    partNumbers = []
    for idx, line in enumerate(lines):
        print("----")
        print("Line ID: " + str(idx))
        symbolPosPrev, symbolPosNext, symbolPosCur = [[]] * 3
        
        digitPos = getDigitPosInLine(line)
        print("All digit positions", digitPos)
        
        if idx != 0:
            symbolPosPrev = getSymbolPosInLine(lines[idx-1])

        symbolPosCur = getSymbolPosInLine(line)
        
        if idx+1 < len(lines):
            symbolPosNext = getSymbolPosInLine(lines[idx+1])

        # Now we have the positions of our numbers on the current line
        # as well as the positions of all the symbols above, below and on the same line
        # now we need to check around each digit for a symbol
        digitsPosWithSymbols = findDigitPosWithSymbols(digitPos, symbolPosPrev, symbolPosCur, symbolPosNext)
        print("digitsPosWithSymbols" , digitsPosWithSymbols)


        p = re.compile(r'\b\d+\b')        
        partNoTemp = []
        errorcheck = []
        for m in p.finditer(line): # this gets all the numbers, but with their position range
            print([m.start(), m.end(), m.group()])
            for y in digitsPosWithSymbols: # for each digitwithsymbol position
                if m.start() <= y < m.end(): #if our position is in the range of the current number positions
                    # only add to list if not already in, this works for duplicates due to also checking range
                    if [m.start(), m.end(), m.group()] not in errorcheck: 
                        errorcheck.append([m.start(), m.end(), m.group()])
                        partNoTemp.append(int(m.group()))

        print("partNumbersTemp", partNoTemp)
        if partNoTemp:
            partNumbers.extend(partNoTemp)
            
    print("\n\n*****************************")       
    print(partNumbers)
    print(sum(partNumbers))
    return sum(partNumbers)


if __name__ == "__main__":
    file1 = open('Day3/extended-testcase.txt', 'r')
    basiclines = file1.readlines()
    if main(basiclines) != 925:
        print("Basic test failed, exiting")
        exit()

    
    input("Anykey to run main file")
    file2 = open('Day3/input.txt', 'r')
    lines = file2.readlines()
    main(lines)
            