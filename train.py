from os import listdir
import pickle
import re
from collections import defaultdict
import argparse


def parse(raw):
    text = re.findall(r"\w+(?:[-]\w+)|\w+", raw)
    return text


def get_dictionary(input_dir):
    last_word = "*START*"
    dic = defaultdict(lambda: defaultdict(int))
    for file in listdir(input_dir):
        input_file = open(input_dir + "\\" + file, "r")
        for line in input_file:
            string = line
            if LC:
                string = string.lower()
            parsed = parse(string)
            for word in parsed:
                dic[last_word][word] += 1
                last_word = word
    dic = dict(dic)
    return dic


parser = argparse.ArgumentParser(description="Command parser")
parser.add_argument("--input-dir", type=str, dest="InputDir", help="The path to the directory where "
                                                                   "is the collection of documents")
parser.add_argument("--model", type=str, dest="Model", help="The path to the file where the model will be saved.")
parser.add_argument("--lc", action="store_true", dest="lc", help="Optional argument. Bring texts to lowercase.")
Command = parser.parse_args(input().split())
LC = Command.lc
Dictionary = get_dictionary(Command.InputDir)
with open(Command.Model, "wb") as outputFile:
    pickle.dump(Dictionary, outputFile)
print("Ready")
outputFile.close()
