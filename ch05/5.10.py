import pandas as pd
import sklearn.datasets as ds
import matplotlib.pyplot as plt
from iris import get_iris_df, df
from pandas.plotting import scatter_matrix

scatter_matrix(df)
plt.show()
