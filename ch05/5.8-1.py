import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

df.plot(kind='scatter', x='sepal length (cm)', y='sepal width (cm)')
plt.title('length vs. width')
plt.show()