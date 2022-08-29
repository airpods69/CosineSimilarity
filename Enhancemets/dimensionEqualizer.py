from typing import List

# Dimension equalization
# Create an vector of equal dimensions for the given two strings

def equalizeDimensions(string1: List, string2: List):
    """
    Create an vector of equal dimensions for the given two strings
    """


    """
    Adds a tuple of the string and 0(False) to the list if the element is not in the list at that index.
    """

    for i in range(len(string1)):

        if type(string2[i]) is tuple:
            continue

        if string1[i] not in string2:
            string1[i] = (string1[i], 0)



    for i in range(len(string2)):

        if type(string1[i]) is tuple:
            pass

        if string2[i] not in string1:
            string2[i] = (string2[i], 0)

    return string1, string2


