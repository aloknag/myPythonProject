import json
import os
from difflib import get_close_matches as gcm


def print_out(meaning):
    for m in meaning:
        print(m)


def find_meaning(word):
    if word.lower() in data.keys():
        print_out(data[word])
    elif word.title() in data.keys():
        print_out(data[word.title()])
    elif word.upper() in data.keys():
        print_out(word.upper())
    else:
        try:
            find_close_match(word)
        except Exception as e:
            print(e)


def find_close_match(w):
    if len(gcm(w, data.keys(), cutoff=0.8)) > 0:
        word = gcm(w, data.keys(), cutoff=0.8)[0]
        if str(input(('Did you mean "%s" instead? :' % word))).lower() in l:
            find_meaning(word)
    else:
        raise Exception('No matching word found')


def get_input():
    try:
        return str(input("Enter the word: "))
    except:
        raise Exception("Bad Input")


if __name__ == "__main__":
    # execute only if run as a script
    curr_dir = os.getcwd()
    l = ['y', 'yes']
    data = json.load(open(curr_dir + '/data.json'))
    word = get_input()
    try:
        find_meaning(word)
    except Exception as e:
        print(e)
