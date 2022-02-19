import json
# from difflib import get_close_matches
from string import ascii_uppercase


def translate(word):
    ch=word[0]
    for i in ascii_uppercase:
        if ch.upper() == i:
            with open('.\dictionary\D'+i+'.json') as f:
                data = json.load(f)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("Wrong search!! Please try again")


word=input("enter a word: ")
output=translate(word)
print(output)

