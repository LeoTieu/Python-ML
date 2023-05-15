import numpy as np

# Creates a 1d array with numbers from 1 to 6
a = np.arange(1,7)

# Use a tuple with dimensions to resize
# This changes to 2 rows, 3 columns
b = a.reshape((2,3))

print(a.shape) # (6,)
# To make it a 1,6 shape. Add an axis.
b = a[np.newaxis, :]
print(b.shape)
