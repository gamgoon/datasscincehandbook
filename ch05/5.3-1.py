import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

sums_by_species = df.groupby('species').sum()
# print(sums_by_species)
var = 'sepal width (cm)'
sums_by_species[var].plot(kind='pie', fontsize=20)
plt.ylabel(var, horizontalalignment='left')
plt.title(var + '로 분류한 붓꽃', fontsize=25)
plt.savefig('iris_pie_for_one_variable.png')
plt.close()