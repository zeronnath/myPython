### ds_ass2-1

# class Myclass:
#     def __init__(self, msg):
#         self.__msg = msg
#     def __str__(self):
#         return 'print : {0}' .format(self.__msg)
#
# c1 = Myclass('test')
# print(c1)


### ds_ass2-2


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import *
from sklearn import *

df = pd.DataFrame({'name': ['Manchester City', 'Manchester United', 'Tottenham Hotspur',
                            'Liverpool', 'Chelsea', 'Arsenal', 'Burnley', 'Everton',
                            'Leicester City', 'Newcastle United', 'Crystal Palace',
                            'Bournemouth', 'West Ham United', 'Watford',
                            'Brighton and Hove Albion', 'Huddersfield Town', 'Southampton',
                            'Swansea City', 'Stoke City', 'West Bromwich Albion'],
                   'gf': [106, 68, 74, 84, 62, 74, 36, 44, 56, 39, 45, 45, 48,
                          44, 34, 28, 37, 28, 35, 31],
                   'ga': [27, 28, 36, 38, 38, 51, 39, 58, 60, 47, 55, 61, 68, 64, 54, 58, 56,
                          56, 68, 56],
                   'points': [100, 81, 77, 75, 70, 63, 54, 49, 47, 44, 44, 44, 42,
                              41, 40, 37, 36, 33, 33, 31]

                   })

df = pd.DataFrame({'name': ['Manchester City', 'Manchester United', 'Tottenham Hotspur',
                            'Liverpool', 'Chelsea', 'Arsenal', 'Burnley', 'Everton',
                            'Leicester City', 'Newcastle United', 'Crystal Palace',
                            'Bournemouth', 'West Ham United', 'Watford',
                            'Brighton and Hove Albion', 'Huddersfield Town', 'Southampton',
                            'Swansea City', 'Stoke City', 'West Bromwich Albion'],
                   'gf': [106, 68, 74, 84, 62, 74, 36, 44, 56, 39, 45, 45, 48,
                          44, 34, 28, 37, 28, 35, 31],
                   'ga': [27, 28, 36, 38, 38, 51, 39, 58, 60, 47, 55, 61, 68, 64, 54, 58, 56,
                          56, 68, 56],
                   'points': [100, 81, 77, 75, 70, 63, 54, 49, 47, 44, 44, 44, 42,
                              41, 40, 37, 36, 33, 33, 31]

                   })
df_x = df[['gf', 'ga']]
df_y = df[['points']]
train_x, test_x, train_y, test_y = train_test_split(df_x, df_y, test_size=0.2, random_state=1234)

model = linear_model.LinearRegression()
model.fit(train_x, train_y)
pred_y = model.predict(test_x)
print("예측값 pred_y=", pred_y)
print("실측값 test_y['points'].values=", test_y['points'].values)
pred_y = np.around(pred_y.flatten()).astype('int')
mae = mean_absolute_error(test_y, pred_y)
print("MAE = ", round(mae, 2))