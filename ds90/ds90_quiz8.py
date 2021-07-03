from sklearn.datasets import load_boston
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

boston = load_boston()

dfX0 = pd.DataFrame(boston.data, columns= boston.feature_names)

dfX = sm.add_constant(dfX0)
dfy = pd.DataFrame(boston.target, columns=["MEDV"])
df = pd.concat([dfX, dfy], axis=1)

model_boston = sm.OLS(dfy, dfX)


result_boston = model_boston.fit()

fig = plt.figure(figsize=(8,20))
sm.graphics.plot_partregress_grid(result_boston, fig=fig)
fig.suptitle("")
plt.show()