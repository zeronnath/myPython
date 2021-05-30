from sklearn.datasets import load_linnerud
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd

### PCA Linnerrud

# iris_df = pd.DataFrame(data = np.c_[Iris['data'], Iris['target']], columns=Iris['feature_names']+['target'])
# iris_df['target'] = iris_df['target'].map({0:"setosa", 1:"versicolor", 2:"virginica"})
#
# X = iris_df.iloc[:, :-1]
# Y = iris_df.iloc[:,[-1]]
#2)
# [[  5. 162.  60. 191.  36.  50.]
#  [  2. 110.  60. 189.  37.  52.]
#  [ 12. 101. 101. 193.  38.  58.]
#  [ 12. 105.  37. 162.  35.  62.]
#  [ 13. 155.  58. 189.  35.  46.]
#  [  4. 101.  42. 182.  36.  56.]
#  [  8. 101.  38. 211.  38.  56.]
#  [  6. 125.  40. 167.  34.  60.]
#  [ 15. 200.  40. 176.  31.  74.]
#  [ 17. 251. 250. 154.  33.  56.]
#  [ 17. 120.  38. 169.  34.  50.]
#  [ 13. 210. 115. 166.  33.  52.]
#  [ 14. 215. 105. 154.  34.  64.]
#  [  1.  50.  50. 247.  46.  50.]
#  [  6.  70.  31. 193.  36.  46.]
#  [ 12. 210. 120. 202.  37.  62.]
#  [  4.  60.  25. 176.  37.  54.]
#  [ 11. 230.  80. 157.  32.  52.]
#  [ 15. 225.  73. 156.  33.  54.]
#  [  2. 110.  43. 138.  33.  68.]]

# # 3)
# [[  4.84819239]
#  [-36.37337868]
#  [-19.71530279]
#  [-48.87880057]
#  [ -1.24439301]
#  [-52.7513643 ]
#  [-59.41274725]
#  [-32.28039126]
#  [ 26.78843143]
#  [192.82401404]
#  [-37.38376798]
#  [ 79.442903  ]
#  [ 79.6880306 ]
#  [-99.21237644]
#  [-85.61627864]
#  [ 76.83255115]
#  [-94.42592828]
#  [ 76.29783425]
#  [ 68.59828074]
#  [-38.02550839]]
#
# 4)
# [[  5. 162.  60. 191.  36.  50.]
#  [  2. 110.  60. 189.  37.  52.]
#  [ 12. 101. 101. 193.  38.  58.]
#  [ 12. 105.  37. 162.  35.  62.]
#  [ 13. 155.  58. 189.  35.  46.]
#  [  4. 101.  42. 182.  36.  56.]
#  [  8. 101.  38. 211.  38.  56.]
#  [  6. 125.  40. 167.  34.  60.]
#  [ 15. 200.  40. 176.  31.  74.]
#  [ 17. 251. 250. 154.  33.  56.]
#  [ 17. 120.  38. 169.  34.  50.]
#  [ 13. 210. 115. 166.  33.  52.]
#  [ 14. 215. 105. 154.  34.  64.]
#  [  1.  50.  50. 247.  46.  50.]
#  [  6.  70.  31. 193.  36.  46.]
#  [ 12. 210. 120. 202.  37.  62.]
#  [  4.  60.  25. 176.  37.  54.]
#  [ 11. 230.  80. 157.  32.  52.]
#  [ 15. 225.  73. 156.  33.  54.]
#  [  2. 110.  43. 138.  33.  68.]]
# [[  9.68240123 149.40974964  73.12363867 177.85161938  35.28616082
#    56.1855779 ]
#  [  7.70641862 116.59237538  49.11575846 184.21469709  36.2540741
#    55.45795509]
#  [  8.50493424 129.85422583  58.81759854 181.64330962  35.86293004
#    55.75199522]
#  [  7.10696316 106.63654159  41.83246811 186.1450692   36.54771075
#    55.23721556]
#  [  9.39034922 144.55931212  69.57525231 178.79208801  35.42921928
#    56.07803459]
#  [  6.92132931 103.55351078  39.57704592 186.74284904  36.63864144
#    55.16885898]
#  [  6.60201163  98.25024137  35.69738584 187.77111885  36.79505568
#    55.05127554]
#  [  7.90261862 119.8508902   51.49955775 183.58289203  36.1579677
#    55.53020248]
#  [ 10.73412075 166.87684314  85.9018666  174.46486234  34.77098762
#    56.57285616]
#  [ 18.69314353 299.06132114 182.60275097 148.83514259  30.87234812
#    59.50363423]
#  [  7.65798496 115.78798285  48.52729701 184.37066362  36.2777988
#    55.4401202 ]
#  [ 13.25814681 208.79619397 116.56838932 166.33696994  33.5346213
#    57.50228687]
#  [ 13.26989716 208.9913453  116.71115423 166.29913135  33.52886552
#    57.50661375]
#  [  4.69419072  66.56490544  12.51765966 193.91470161  37.7295807
#    54.34875215]
#  [  5.34592844  77.38904966  20.43617123 191.8159697   37.41033417
#    54.58874375]
#  [ 13.13301791 206.71803705 115.04809272 166.7399112   33.59591431
#    57.45621023]
#  [  4.9236322   70.37549919  15.30533784 193.175852    37.61719133
#    54.43324017]
#  [ 13.10738592 206.29233749 114.73666792 166.8224516   33.60846986
#    57.44677168]
#  [ 12.73830285 200.16255828 110.25236629 168.01097635  33.78926113
#    57.31086296]
#  [  7.62722272 115.27707959  48.15354059 184.46972448  36.29286734
#    55.42879251]]

# 5)
# 0.78


ll = load_linnerud()
print(ll.DESCR)


