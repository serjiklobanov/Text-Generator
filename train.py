command = input()
while command != "":
    command = command.split()
    if "--help" in command:
        helps = open("trainHelp.txt", 'r')
        for line in helps:
            print(line, end='')
        print()
    lc = False
    if "--lc" in command:
        lc = True
    lastWord = ""
    dictionary = {}
    if "--input-dir" in command:
        inputDir = command[command.index("--input-dir") + 1]
        inputFile = open(inputDir + "\\" + input("Select input text file:"), 'r')
        for line in inputFile:
            string = line
            if lc:
                string = string.lower()
            string = string.split()
            for word in string:
                newWord = ""
                for char in word:
                    if (64 < ord(char) < 91) or (96 < ord(char) < 123) or (1039 < ord(char) < 1104) \
                            or (ord(char) == 1105) or (ord(char) == 1025):
                        newWord = newWord + char
                if newWord != "":
                    if lastWord != "":
                        if newWord in dictionary[lastWord].keys():
                            dictionary[lastWord][newWord] += 1
                        else:
                            dictionary[lastWord].update({newWord: 1})
                    if newWord not in dictionary.keys():
                        dictionary.update({newWord: {}})
                    lastWord = newWord
    else:
        string = input()
        while string != "":
            if lc:
                string = string.lower()
            string = string.split()
            for word in string:
                newWord = ""
                for char in word:
                    if (64 < ord(char) < 91) or (96 < ord(char) < 123) or (1039 < ord(char) < 1104) \
                            or (ord(char) == 1105) or (ord(char) == 1025):
                        newWord = newWord + char
                if newWord != "":
                    if lastWord != "":
                        if newWord in dictionary[lastWord].keys():
                            dictionary[lastWord][newWord] += 1
                        else:
                            dictionary[lastWord].update({newWord: 1})
                    if newWord not in dictionary.keys():
                        dictionary.update({newWord: {}})
                    lastWord = newWord
            string = input()
    model = command[command.index("--model") + 1]
    outputFile = open(model, 'w')
    for word1 in dictionary.keys():
        outputFile.write(word1 + '\n')
        for word2 in dictionary[word1].keys():
            outputFile.write(word2 + ' ' + str(dictionary[word1][word2]) + '\n')
    outputFile.close()
    command = input()
