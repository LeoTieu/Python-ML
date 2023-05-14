import numpy as np
print(np.__version__)

a = np.array([1,2,3])
# Prints the array
print(a)

# Prints a tuple of the array shape
print(a.shape)

# Prints the type of element
print(a.dtype)

# Prints dimensions
print(a.ndim)

# Prints the size of the array
print(a.size)

# Mathematical operations / changing the array
a[0] = 10

b = a * np.array([2,0,2])
print(b)