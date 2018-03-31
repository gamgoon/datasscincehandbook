import pandas as pd
import sklearn.datasets as ds
import matplotlib.pyplot as plt
from iris import get_iris_df, df

df.plot(kind='hexbin', x='sepal length (cm)', y='sepal width (cm)')
plt.show()
