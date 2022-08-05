import numpy as np
from tqdm import tqdm

with open('Dataset/glove.6B.50d.txt', 'r') as file:
    data = file.readlines()

print("Data loaded")

# No clue why this exists -> forgot to document it
for i in range(len(data)):
    data[i] = data[i][:-1]

print("Data split")

# Add all codes to a dictionary
data_dict = dict()

for i in tqdm(range(len(data))):

    split_data = data[i].split()
    data_dict[split_data[0]] = np.array(split_data[1:]).astype('float64')

print("Data dictionarized")

class Enhancement:
    """
    Class for Enhancement according the paper Section IIIB
    """

    def __init__(self, s1, s2):
        self.s1 = s1.lower().split()
        self.s2 = s2.lower().split()

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

    def norm(self, s):
        return np.sqrt(np.sum((data_dict[s]**2)))


    def cosine_similarity(self):
        """
        Cosine similarity of the two strings
        """

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


obj = Enhancement('This table is Stupid', 'This desk is stupid')

print(obj.cosine_similarity())




