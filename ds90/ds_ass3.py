import numpy as np


### ass3: Euclid distance

def eculid_distance(a: list, b: list):
    c = list()
    for i in range(len(a)):
        c.append(a[i] - b[i])
    print(c)
    for i in range(len(c)):
        c[i] = c[i] * c[i]
    print(c)

    distance = np.sum(c)
    distance = np.sqrt(distance)
    return distance


print(eculid_distance([33, 17, 50, 106, 3], [26, 20, 30, 88, 2]))
a = np.array([33, 17, 50, 106, 3])
b = np.array([26, 20, 30, 88, 2])
dist = np.linalg.norm(a - b)
print("euclid dist=",dist)


### euclid distance
# np.linalg.norm(a - b)
# 두 벡터의 내적은 np.dot(a, b)

from numpy import dot
from numpy.linalg import norm
import numpy as np
a = np.array([33, 17, 50, 106, 3])
b = np.array([26, 20, 30, 88, 2])

euclid_dist = np.linalg.norm(a - b)

cos_dist = 1 - (dot(a,b)/(norm(a)*norm(b)))
print("euclid dist=",euclid_dist)
print("cosine dist=",cos_dist)

### ass3: cosign distance
