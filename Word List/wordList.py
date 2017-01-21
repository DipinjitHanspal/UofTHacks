wordList = []

fOpen = open("dictionary.csv", "r")
for line in fOpen:
    wordList.append(line.strip("\n").strip("\r"))
fOpen.close()
