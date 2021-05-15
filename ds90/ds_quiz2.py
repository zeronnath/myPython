def map_func(func, *args):
    return [func(datas) for datas in zip(*args )]

ls1= [1,2,3]
ls2=[3,5,7]
ls3=[6,5,4]
print(map_func(lambda v: sum(v), (1,) ) )

for i in (3,2):
    print(i)

from cote.pkg.t_1 import prt, prt2
prt2('')

import numpy as np
import pandas as pd

np.random.seed(0)
dt = pd.Series(np.random.randint(1,10, size=5), index=list('ABCDE'))
res = dt+2
res['B'] =10
res+=3
print(res['B'])