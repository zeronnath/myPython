from pgmpy.factors.discrete import JointProbabilityDistribution  as JPD
import numpy as np

pxy = JPD((['X', 'Y']), [2, 2], np.array([3, 9, 7, 1]) / 20)
pmx = pxy.marginal_distribution(['X'], inplace=False)

print(pxy)
print(pmx)