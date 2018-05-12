import random
import pickle
import argparse


def get_population(dic):
    return tuple(dic.keys())


def get_weights(dic):
    weights = []
    for word in get_population(dic):
        weights += [dic[word]]
    return tuple(weights)


parser = argparse.ArgumentParser(description="Command parser")
parser.add_argument("--seed", type=str, dest="Seed", help="Optional argument. The initial word. If not specified, "
                                                          "select the word randomly from all words (not including the "
                                                          "frequency).")
parser.add_argument("--model", type=str, dest="Model", help="The path to the file from which the model will be loaded.")
parser.add_argument("--length", type=int, dest="length", help="Length of the generated sequence.")
parser.add_argument("--output", dest="output", help="Optional argument. The file to which the result will be recorded."
                                                    " If there is no argument, output to stdout.")
while True:
    Command = parser.parse_args(input().split())
    with open(Command.Model, "rb") as inputFile:
        Dictionary = pickle.load(inputFile)
    if Command.Seed is not None:
        Seed = Command.Seed
    else:
        Seed = random.choice(list(Dictionary.keys()))
    if Command.output is not None:
        output = open(Command.output, "w")
        for i in range(Command.length):
            output.write(Seed + ' ')
            Seed = random.choices(get_population(Dictionary[Seed]), weights=get_weights(Dictionary[Seed]), k=1)[0]
            output.write(Seed + ' ')
            if (i + 1) % 20 == 0:
                output.write('\n')
        output.close()
    else:
        print(Seed, end=' ')
        for i in range(Command.length):
            Seed = random.choices(get_population(Dictionary[Seed]), weights=get_weights(Dictionary[Seed]), k=1)[0]
            print(Seed, end=' ')
            if (i + 1) % 20 == 0:
                print()
