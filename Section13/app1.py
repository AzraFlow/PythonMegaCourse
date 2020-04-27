#! python3

import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), n=1, cutoff=0.8)) > 0:
        match = get_close_matches(w, data.keys(), n=1, cutoff=0.8)
        yn = input(f'Did you mean {match[0]}? (Y/N)  ')
        if yn.upper() == 'Y':
            return data[match[0]]
        elif yn.upper() == "N":
            return "No close match found for word entered."
        else:
            return "We didn't understand your answer."
    else:
        return "Word doesn't exist, please enter another word."


word = input('Enter word:  ')

definitions = translate(word)

if type(definitions) == list:
    for definition in definitions:
        print(definition)
else:
    print(definitions)
