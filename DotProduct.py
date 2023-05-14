# Chat-GPT3:
# If we have two vectors A and B, 
# where A = [a1, a2, a3] and B = [b1, b2, b3], then the dot product of A and B is given by:
#A · B = a1b1 + a2b2 + a3b3
import numpy as np


a1 = np.array([1,2,3])
a2 = np.array([4,5,6])

# Numpy dot function
dot = np.dot(a1,a2)
print(dot)  # 32

# 2nd optional one liner
dot = (a1 * a2).sum()

# 3rd optional one liner
dot = a1 @ a2

# Manual
sum1 = a1 * a2
dot = np.sum(sum1)

