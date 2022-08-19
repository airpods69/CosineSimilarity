from nltk.corpus import wordnet

def hypernyms(word):
    syns = wordnet.synsets(word)

    hypernymsList = []

    for hypernym in syns:
        hypernymsList.append(hypernym.name().split('.')[0])

    print(hypernymsList)

hypernyms('dog')
