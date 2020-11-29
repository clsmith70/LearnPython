import numpy as np

# create a list of weights in kg
weight_kg = [81.65, 9.52, 95.25, 92.98, 86.18, 88.45]

# create a numpy array of the weights
np_weight_kg = np.array(weight_kg)

# create a numpy array of weights converted to lbs
np_weight_lbs = np_weight_kg ** 2.2

# print the result
print(np_weight_lbs)