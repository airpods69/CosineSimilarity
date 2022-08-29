from typing import List
from nltk.corpus import wordnet

def hypernyms(word):
    """
    Use wordnet corpus to find the hypernyms for a specific word
    Args:
        input: String word

        output: List of hypernyms
    """

    syns = wordnet.synsets(word)

    if syns == []:
        return None

    hypernymsList = []
    for syn in syns:
        hypernymsList.append(syn.hypernyms()[0].name())

    return [hypernyms.split('.')[0] for hypernyms in hypernymsList]


def addHypernyms(string1: List, string2: List):
    """
    Takes in the two strings and returns both strings where string2 has
    """
    for i in string1:

        hypernymList = hypernyms(i)
        if hypernymList is None:
            continue


        for j in range(len(string2)):

            # If hyponym of i is in string2 then replace it with a tuple (j, i) and while dimension equalization check for i so that it doesnt get equaliated with 0
            # But norm of i, j

            if string2[j] in hypernymList:

                string2[j] = (string2[j], i)

    return string1, string2

string1 = "Your cat is pretty"
string2 = "Your feline is nice"

print(addHypernyms(string1.split(), string2.split()))
