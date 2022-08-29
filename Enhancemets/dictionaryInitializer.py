from tqdm import tqdm
import numpy as np

def dictionaryInitializer():
        with open('Enhancemets/Dataset/glove.6B.50d.txt', 'r') as file:
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

        return data_dict