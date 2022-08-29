from enhancer import enhancer
from dictionaryInitializer import dictionaryInitializer

from norm import norm
import numpy as np

from typing import List



string1 = "Your dog is pretty".lower().split()
string2 = "Your dog is beautiful".lower().split()



string1, string2 = enhancer(string1, string2)

data_dict = dictionaryInitializer()


def cosine_similarity(s1: List, s2: List, data_dict):

    # Numerator

    numerator = 0

    for i in range(len(s1)):
        if type(s1[i]) is tuple or type(s2[i]) is tuple:
            continue

        numerator += norm(s1[i], data_dict) * norm(s2[i], data_dict)

        denominator1, denominator2 = 0, 0

        for i in range(len(s1)):

            if type(s1[i]) is tuple :
                denominator1 += norm(s1[i][0], data_dict)**2
            else:
                denominator1 += norm(s1[i], data_dict)**2

            print("type of {} is {}".format(s2[i],type(s2[i])))

            if type(s2[i]) is np.float64:
                denominator2 += s2[i]**2
            elif type(s2[i]) is tuple:
                denominator2 += norm(s2[i][0], data_dict)**2
            else:
                denominator2 += norm(s2[i], data_dict)**2

        denominator = np.sqrt(denominator1) * np.sqrt(denominator2)



    return numerator/denominator

print(cosine_similarity(string1, string2, data_dict))


                
