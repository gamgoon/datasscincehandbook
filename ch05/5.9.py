import pandas as pd
import sklearn.datasets as ds
import matplotlib.pyplot as plt

bs = ds.load_boston()
df = pd.DataFrame(bs.data, columns=bs.feature_names)
df['MEDV'] = bs.target
# print(df)
df.plot(x='CRIM', y='MEDV', kind='scatter', logx=True)
plt.title('aaa')
plt.show()