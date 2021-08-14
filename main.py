import json
import difflib

data = json.load(open('data.json'))

def translate():
    while True:
        word = input('Enter word: ')
        word = word.lower()
        if (word in data):
            display(word, data)
        elif (word.capitalize() in data):
            word = word.capitalize()
            display(word, data)
        elif (word.upper() in data):
            word = word.upper()
            display(word, data)
        elif (len(difflib.get_close_matches(word, data, n=1, cutoff=0.7)) == 1):
            ans = difflib.get_close_matches(word, data, n=1, cutoff=0.7)[0]
            yes_no = input(f'Did you mean {ans} y/n: ')
            if (yes_no.lower() == 'y'):
                display(ans, data)
            elif (yes_no.lower() == 'n'):
                print("The word doesn't exist. Please double check it")
            else:
                print('Invalid entry.')
        else:
            print("The word doesn't exist. Please double check it")

def display(word, list):
    if (len(list[word]) == 1):
        print(list[word][0])
    else:
        i = 1
        for w in list[word]:
            print(f"{i}. {w}")
            i = i+1


translate() 