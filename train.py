from os import listdir
import pickle


def parse(w):
    new = ""
    for char in w:
        if (ord('a') <= ord(char)) and (ord(char) <= ord('z')) \
                or (ord('A') <= ord(char)) and (ord(char) <= ord('Z')) \
                or (ord('А') <= ord(char)) and (ord(char) <= ord('Я')):
            new = new + char
    return w


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
            string = string.split()
            for word in string:
                parsed = parse(word)
                if parsed != "":
                    if last_word != "":
                        if parsed in dic[last_word].keys():
                            dic[last_word][parsed] += 1
                        else:
                            dic[last_word].update({parsed: 1})
                    if parsed not in dic.keys():
                        dic.update({parsed: {}})
                    last_word = parsed
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
