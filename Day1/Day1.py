
# Using readlines()
file1 = open('Day1/input.txt', 'r')
Lines = file1.readlines()


words = ["one","two","three","four","five","six","seven","eight","nine"]
wordsNum = [1,2,3,4,5,6,7,8,9]

total = 0;
count = 0
for entry in Lines:
    count += 1
    entryPos = []
    entryWord = []

    # Find positions of each text number
    for word in words:
        result = [i for i in range(len(entry)) if entry.startswith(word, i)]
        start_index = entry.find(word)
        for res in result:
            entryWord.append(wordsNum[words.index(word)])
            entryPos.append(res)   

    # find position of each digit number
    for idx, ch in enumerate(entry):
        if ch.isnumeric():
            entryWord.append(int(ch))
            entryPos.append(idx)

    minPos = entryPos.index(min(entryPos))
    maxPos = entryPos.index(max(entryPos))

    total += int(str(entryWord[minPos]) + str(entryWord[maxPos]))
    
    # Debugging for each loop    
    print(entry)
    print("pos: "+ str(entryPos))
    print("numbers:" + str(entryWord))
    print("minPos: " + str(minPos))
    print("maxPos: " + str(maxPos))
    print("minNumber: " + str(entryWord[minPos]))
    print("maxNumber: " + str(entryWord[maxPos]))
    print(int(str(entryWord[minPos]) + str(entryWord[maxPos])))

print(total)