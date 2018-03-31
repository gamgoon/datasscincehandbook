import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import sklearn.datasets
from iris import get_iris_df, df

df.plot(kind='hist', subplots=True, layout=(2,2))
plt.suptitle('iris histogram', fontsize=20)
plt.show()