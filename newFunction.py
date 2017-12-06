import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def findMeaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8))>0:
        s= get_close_matches(word,data.keys(),cutoff=0.8)[0]
        yn=input("Did you mean '"+s+"' ? If yes the enter Y, if no then enter N:\n")
        if yn=='Y':
            return data[s]
        else:
            return "Sorry. Please enter the correct word again."

    else:
        return "The word that you want to find is not in the dictionary. Please double check."


word=input("Enter a word:\n")
print(findMeaning(word))