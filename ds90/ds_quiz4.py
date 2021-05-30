
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
Iris = load_iris()
iris_df = pd.DataFrame(data = np.c_[Iris['data'], Iris['target']], columns=Iris['feature_names']+['target'])
iris_df['target'] = iris_df['target'].map({0:"setosa", 1:"versicolor", 2:"virginica"})

X = iris_df.iloc[:, :-1]
Y = iris_df.iloc[:,[-1]]
