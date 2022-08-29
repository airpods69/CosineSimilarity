import numpy as np

def norm(s, data_dict):
    return np.sqrt(np.sum((data_dict[s]**2)))