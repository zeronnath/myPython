import numpy as np
x2=np.array([[1,3,5],[2,3,7], [9,1,2], [4,8,7],[6,5,2]])
print(np.linalg.matrix_rank(x2))

A = np.array([ [2,-2], [0,-3]])
w1, v1 = np.linalg.eig(A)
print("w1", w1)
print("v1", v1)

