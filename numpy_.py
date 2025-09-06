import numpy as np

data = [[0.5, 3, 2]]

array_from_data = np.array(data, dtype=np.float32)

#Zeros and Ones
zeros = np.zeros((32, 32, 3))
zeros = np.zeros_like(zeros)
ones = np.ones((32, 32, 3))
ones = np.ones_like(ones)

#Random
np.random.seed = 1234
random_floats = np.random.rand((ones.shape))
random_ints = np.random.randint((ones.shape))
#random_sample
