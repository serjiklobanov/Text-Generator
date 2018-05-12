from os import listdir
import pickle
import re


def parse(raw):
    text = re.findall(r"\w+(?:[-]\w+)|\w+", raw)
    return text


def print_help():
    helps = open("generateHelp.txt", 'br').read()
    helps = helps.decode('utf8')
    for l in helps:
        print(l, end='')
    print()


def get_dictionary(input_dir):
    last_word = ""
    dic = {}
    for file in listdir(input_dir):
        input_file = open(input_dir + '\\' + file, 'r')
        for line in input_file:
            string = line
            if LC:
                string = string.lower()
            parsed = parse(string)
            for word in parsed:
                if last_word != "":
                    if word in dic[last_word].keys():
                        dic[last_word][word] += 1
                    else:
                        dic[last_word].update({word: 1})
                if word not in dic.keys():
                    dic.update({word: {}})
                last_word = word
    return dic


Command = input()
while Command != "":
    Command = Command.split()
    if "--help" in Command:
        print_help()
    else:
        LC = False
        if "--lc" in Command:
            LC = True
        InputDir = Command[Command.index("--input-dir") + 1]
        Model = Command[Command.index("--model") + 1]
        Dictionary = get_dictionary(InputDir)
        with open(Model, "wb") as outputFile:
            pickle.dump(Dictionary, outputFile)
        print('Ready')
        outputFile.close()
    Command = input()
