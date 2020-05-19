import json
from difflib import get_close_matches

def definition(word):
    if word in data.keys():
        return data[word]
    else:
        return check_word(word)

def check_word(word):
    word = word.lower()
    close = get_close_matches(word, data.keys())
    if word.title() in data.keys():
        return(data[word.title()])
    elif word.upper() in data.keys():
        return(data[word.upper()])
    elif len(close) > 0:
        answer = input(f"Did you mean {close[0]} instead? Enter Y for yes, or N for no. ")
        if answer.upper() == 'Y':
            return data[close[0]]
        elif answer.upper() == 'N':
            return "The word does not exist. Please double check word."
        else:
            return "Did not understand your entry"  

data = json.load(open("data.json"))
exit=''

while True:
    if exit != "exit":
        word = input("Enter word: ")
        output = definition(word)
        if type(output) == list:
            count = 1
            for item in output:
                print(f"{count}. {item}")
                count+=1
        else:
            print(output)
    else:
        break
    exit = input("Please type \'exit\' to quit otherwise press any key to continue: ")