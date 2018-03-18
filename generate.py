import random
command = input()
while command != "":
    command = command.split()
    if "--help" in command:
        helps = open("generateHelp.txt", 'r')
        for line in helps:
            print(line, end='')
        print()
    model = command[command.index("--model") + 1]
    inputFile = open(model, 'r')
    dictionary = {}
    for line in inputFile:
        string = line.split()
        if len(string) == 1:
            dictionary.update({string[0]: []})
            word1 = string[0]
        else:
            dictionary[word1] += [string[0]] * int(string[1])
    if "--seed" in command:
        seed = command[command.index("--seed") + 1]
    else:
        seed = random.choice(list(dictionary.keys()))
    length = int(command[command.index("--length") + 1])
    print(seed, end=' ')
    if "--output" in command:
        output = open(command[command.index("--output") + 1])
        for i in range(length):
            seed = random.choice(dictionary[seed])
            output.write(seed + ' ')
            if (i + 1) % 20 == 0:
                output.write('\n')
    else:
        for i in range(length):
            seed = random.choice(dictionary[seed])
            print(seed, end=' ')
            if (i + 1) % 20 == 0:
                print()
    command = input()
