import numpy as np

a = np.array([[1,2],[3,4]])


# Accessing elements
print(a[0][0])
print(a[0,0])

# Access all rows and only column 0
print(a[:,0])

# Transpose array
print(a.T)

# Inverse of array. Array must be a square
print(np.linalg.inv(a))

# Calculate determinant of array.
print(np.linalg.det(a))

# Get the diagonal elements of the array.
print(np.diag(a))