import dimensionEqualizer
import synonymPair
import hypernymHyponym
from typing import List


def removeStopWords(string1: List, string2: List):

    stopwords = ["ourselves", "hers", "between", "yourself", "but", "again", "there", "about", "once", "during", "out", "very", "having", "with", "they", "own", "an", "be", "some", "for", "do", "its", "yours", "such", "into", "of", "most", "itself", "other", "off", "is", "s", "am", "or", "who", "as", "from", "him", "each", "the", "themselves", "until", "below", "are", "we", "these", "your", "his", "through", "don", "nor", "me", "were", "her", "more", "himself", "this", "down", "should", "our", "their", "while", "above", "both", "up", "to", "ours", "had", "she", "all", "no", "when", "at", "any", "before", "them", "same", "and", "been", "have", "in", "will", "on", "does", "yourselves", "then", "that", "because", "what", "over", "why", "so", "can", "did", "not", "now", "under", "he", "you", "herself", "has", "just", "where", "too", "only", "myself", "which", "those", "i", "after", "few", "whom", "t", "being", "if", "theirs", "my", "against", "a", "by", "doing", "it", "how", "further", "was", "here", "than"]

    string1_new, string2_new = [], []


    for i in range(len(string1)):
        if string1[i] in stopwords:
            continue

        string1_new.append(string1[i])

    for i in range(len(string2)):
        if string2[i] in stopwords:
            continue

        string2_new.append(string2[i])

    return string1_new, string2_new


def enhancer(string1: List, string2: List):

    print(string1, string2)

    string1, string2 = removeStopWords(string1, string2)

    string1, string2 = synonymPair.getSynonyms(string1, string2)
    string1.sort()
    string2.sort()
    string1, string2 = hypernymHyponym.addHypernyms(string1, string2)
    string1, string2 = dimensionEqualizer.equalizeDimensions(string1, string2)

    return string1, string2
