import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

sums_by_species = df.groupby('species').sum()
# print(sums_by_species)
sums_by_species.plot(kind='pie', subplots=True,
layout=(2,2), legend=False)

plt.title('종에 따른 전체 측정값')
plt.savefig('iris_pie_for_each_variable.png')
plt.close()