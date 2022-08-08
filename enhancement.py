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

    def replaceSynonyms(self):
        """
        Replace words with their synonyms in the two strings
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

    # Synonym Part done

    # Finding and replacing Hypernym

    def getHypernym(self, word):

        # Finding Hypernym using NLTK and adding all the hypernyms which are present in self.s1 and self.s2 to a list
        def hypernym(word):
            from nltk.corpus import wordnet as wn
            hypernyms = []
            for syn in wn.synsets(word):
                for hypernym in syn.hypernyms():
                    hypernyms.append(hypernym.name().split('.')[0])
            return hypernyms

        L = []
        L_hypernyms = [x.replace(' ', '') for x in hypernym(word)]

        for i in L_hypernyms:
            if i not in self.s1 and i not in self.s2:
                continue
            else:
                L.append(i)

        return L

    def replaceHypernyms(self):
        """
        Replace words with their hypernyms in the two strings
        """

        for i in range(len(self.s1)):

            if self.getHypernym(self.s1[i]) == []:
                continue
            else:
                self.s2[self.s2.index(self.getHypernym(self.s1[i])[0])] = self.s1[i]

        for i in range(len(self.s2)):

            if self.getHypernym(self.s2[i]) == []:
                continue
            else:
                hyp = self.getHypernym(self.s2[i])[0]
                ind = self.s1.index(hyp)
                self.s1[ind]= self.s2[i]

        return self.s1, self.s2

    def recalibrateHypernyms(self):

        # self.dictionaryInitializer()

        for i in range(len(self.s1)):

            try:

                if type(self.s1[i]) is tuple:
                    hyp = self.getHypernym(self.s1[i][0])[0]
                else:
                    hyp = self.getHypernym(self.s1[i])[0]

                ind = self.s2.index(hyp)
                self.s2[ind]= self.norm(self.getHypernym(self.s1[i])[0]) * self.norm(self.s1[i])


                # self.s2[self.s2.index(self.getHypernym(self.s1[i])[0])] = self.norm(self.getHypernym(self.s1[i])[0]) * self.norm(self.s1[i])
            except IndexError:
                continue

        return self.s1, self.s2


    # Norm to find the vector of the work/string
    def norm(self, s):
        return np.sqrt(np.sum((self.data_dict[s]**2)))

    def cosine_similarity(self):
        """
        Cosine similarity of the two strings
        """

        self.dictionaryInitializer()
        self.replaceSynonyms()
        # self.replaceHypernyms()
        # Dimension equalization
        self.dimensionEqualization()
        self.recalibrateHypernyms()

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

            if type(self.s2[i]) is float:
                denominator2 += self.s2[i]**2
            elif type(self.s2[i]) is tuple:
                denominator2 += self.norm(self.s2[i][0])**2
            else:
                denominator2 += self.norm(self.s2[i])**2

        denominator = np.sqrt(denominator1) * np.sqrt(denominator2)

        return numerator / denominator


# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

string1 = "cat mouse tom jerry"
string2 = "rodent jerry"

obj = Enhancement(string1, string2)
print(obj.cosine_similarity())
# print(obj.replaceSynonyms())
# print(obj.replaceHypernyms())
# print(obj.recalibrateHypernyms())
