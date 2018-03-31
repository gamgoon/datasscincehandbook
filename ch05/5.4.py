import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

sums_by_species = df.groupby('species').sum()
# print(sums_by_species)
var = 'sepal width (cm)'
sums_by_species[var].plot(kind='bar', fontsize=15, rot=30)

plt.title(var + '로 분류한 붓꽃', fontsize=20)
plt.savefig('iris_bar_for_one_variable.png')
plt.close()

sums_by_species = df.groupby('species').sum()
sums_by_species.plot(kind='bar', subplots=True, fontsize=12)

plt.suptitle('종에 따른 전체 측정값')
plt.savefig('iris_bar_for_each_variable.png')
plt.close()