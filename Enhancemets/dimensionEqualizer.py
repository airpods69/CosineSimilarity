# Dimension equalization
# Create an vector of equal dimensions for the given two strings

def equalizeDimensions(string1, string2):
    """
    Create an vector of equal dimensions for the given two strings
    """

    string1 = string1.split()
    string2 = string2.split()

    if len(string1) > len(string2):
        """
        Adds a tuple of the string and 0(False) to the list if the element is not in the list at that index.
        """

        for i in string1:
            if i not in string2:
                string2.append((i, 0))

    else:

        for i in string2:
            if i not in string1:
                string1.append((i, 0))

    return string1, string2


