import random
import pickle


def print_help():
    helps = open("generateHelp.txt", 'br').read()
    helps = helps.decode('utf8')
    for l in helps:
        print(l, end='')
    print()


def parse_dictionary(dic):
    new_dictionary = {}
    for word1 in dic.keys():
        new_dictionary.update({word1: []})
        for word2 in dic[word1].keys():
            new_dictionary[word1] += [word2] * dic[word1][word2]
    return new_dictionary


Command = input()
while Command != "":
    Command = Command.split()
    if "--help" in Command:
        print_help()
    else:
        model = Command[Command.index("--model") + 1]
        with open(model, "rb") as inputFile:
            Dictionary = pickle.load(inputFile)
        NewDictionary = parse_dictionary(Dictionary)
        if "--seed" in Command:
            seed = Command[Command.index("--seed") + 1]
        else:
            seed = random.choice(list(NewDictionary.keys()))
        length = int(Command[Command.index("--length") + 1])
        print(seed, end=' ')
        if "--output" in Command:
            output = open(Command[Command.index("--output") + 1])
            for i in range(length):
                seed = random.choice(NewDictionary[seed])
                output.write(seed + ' ')
                if (i + 1) % 20 == 0:
                    output.write('\n')
        else:
            for i in range(length):
                seed = random.choice(NewDictionary[seed])
                print(seed, end=' ')
                if (i + 1) % 20 == 0:
                    print()
    Command = input()
