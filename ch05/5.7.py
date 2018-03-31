import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

col = 'sepal width (cm)'
df['ind'] = pd.Series(df.index).apply(lambda i: i% 50)
df.pivot('ind', 'species')[col].plot(kind='box')
plt.show()