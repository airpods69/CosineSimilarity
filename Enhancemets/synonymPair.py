# Find synonyms using thesaurus.com

import requests
from typing import List
from bs4 import BeautifulSoup

def synonymPair(string1):
    """
    returns a list of synonyms for the given string from thesaurus.com
    """

    response = requests.get("http://www.thesaurus.com/browse/" + string1)
    soup = BeautifulSoup(response.text, "lxml")
    soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
    return [span.text.replace(' ', '') for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})]

def getSynonyms(string1: List, string2: List):
    """
    returns a list of synonyms for the given string which exist in either of the strings
    """

    for i in string1:

        syms = synonymPair(i)

        for j in range(len(string2)):
            # Loop through elements of string2 to check if it exists in the synonyms list
            # and replace it with the first dimension term

            if string2[j] in syms:
                string2[j] = i

    return string1, string2
