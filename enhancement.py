import numpy as np
from tqdm import tqdm


class Enhancement:
    """
    Class for Enhancement according the paper Section IIIB
    """

    def __init__(self, s1, s2):
        self.s1 = s1.lower().split()
        self.s2 = s2.lower().split()

    def dictionaryInitializer(self):
        with open('Dataset/glove.6B.50d.txt', 'r') as file:
            data = file.readlines()

        print("Data loaded")

        # No clue why this exists -> forgot to document it
        for i in range(len(data)):
            data[i] = data[i][:-1]

        print("Data split")

        # Add all codes to a dictionary
        self.data_dict = dict()

        for i in tqdm(range(len(data))):
            split_data = data[i].split()
            self.data_dict[split_data[0]] = np.array(split_data[1:]).astype('float64')

        print("Data dictionarized")



    def dimensionEqualization(self):
        """
        Dimension equalization of the List of string passed
        """

        for i in range(len(self.s2)):

            if self.s2[i] not in self.s1:
                self.s1.insert(i, (self.s2[i], 0))

        for i in range(len(self.s1)):

            if type(self.s1[i]) is tuple:

                if self.s1[i][0] not in self.s2:
                    self.s2.insert(i, (self.s1[i][0], 0))

            else:
                if self.s1[i] not in self.s2:
                    self.s2.insert(i, (self.s1[i], 0))


    # Get Synonym of the word
    def getSynonym(self, word):

        import requests
        from bs4 import BeautifulSoup

        def synonyms(term):
            response = requests.get('https://www.thesaurus.com/browse/{}'.format(term))
            soup = BeautifulSoup(response.text, 'lxml')
            soup.find('section', {'class': 'css-17ofzyv e1ccqdb60'})
            return [span.text for span in soup.findAll('a', {'class': 'css-1kg1yv8 eh475bn0'})] # 'css-1gyuw4i eh475bn0' for less relevant synonyms

        L = []
        L_synoyms = [x.replace(' ', '') for x in synonyms(word)]


        for i in L_synoyms:
            if i not in self.s1 and i not in self.s2:
                continue
            else:
                L.append(i)

        return L

    def replaceWords(self):
        """
        Replace words in the two strings
        """

        for i in range(len(self.s1)):

            if self.getSynonym(self.s1[i]) == []:
                continue
            else:
                self.s2[self.s2.index(self.getSynonym(self.s1[i])[0])] = self.s1[i]

        for i in range(len(self.s2)):

            if self.getSynonym(self.s2[i]) == []:
                continue
            else:
                self.s1[self.s1.index(self.getSynonym(self.s2[i])[0])] = self.s2[i]

    # Norm to find the vector of the work/string
    def norm(self, s):
        return np.sqrt(np.sum((self.data_dict[s]**2)))

    def cosine_similarity(self):
        """
        Cosine similarity of the two strings
        """

        self.dictionaryInitializer()
        self.replaceWords()
        # Dimension equalization
        self.dimensionEqualization()

        print("New values of s1 and s2: \n", self.s1, "\n", self.s2)

        # Calculate the cosine similarity
        numerator = 0
        for i in range(len(self.s1)):

            if type(self.s1[i]) is tuple or type(self.s2[i]) is tuple:
                continue
            numerator += self.norm(self.s1[i]) * self.norm(self.s2[i])

        denominator1, denominator2 = 0, 0

        for i in range(len(self.s1)):

            if type(self.s1[i]) is tuple :
                denominator1 += self.norm(self.s1[i][0])**2
            else:
                denominator1 += self.norm(self.s1[i])**2

            if type(self.s2[i]) is tuple:
                denominator2 += self.norm(self.s2[i][0])**2
            else:
                denominator2 += self.norm(self.s2[i])**2

        denominator = np.sqrt(denominator1) * np.sqrt(denominator2)

        return numerator / denominator


obj = Enhancement('This desk is not stupid', 'This table is stupid')
print(obj.cosine_similarity())
# print(obj.replaceWords())

