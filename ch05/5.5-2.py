import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
from iris import get_iris_df, df

for spec in df['species'].unique():
    forspec = df[df['species']==spec]
    forspec['petal length (cm)'].plot(kind='hist', alpha=0.4, label=spec)

plt.legend(loc='upper right')
plt.suptitle('petal length by species')
plt.savefig('iris_hist_by_spec.png')