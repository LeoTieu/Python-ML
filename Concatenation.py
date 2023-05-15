import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6]])

# Concatenates a and b
c = np.concatenate((a,b))
print(c.shape) # (3, 2)

# Default axis is 0
# However, changing manually is possible.
c = np.concatenate((a,b), axis=None)
print(c.shape) # (6,)

c = np.concatenate((a,b.T), axis=1)
print(c.shape) # (2, 3)

# hstack and vstack
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
v = np.vstack((a,b))
h = np.hstack((a,b))
print(v.shape) # (2, 4)
print(h.shape) # (8,)